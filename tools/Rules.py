import json
import csv
import yaml


rules = []
last_rule = None

def load_yaml(file):
    with open(file) as f:
        data_map = yaml.safe_load(f)

def load(file):
    with open(file) as cfile:
        creader = csv.reader(cfile)
        line_count = 0
        for row in creader:
            if line_count is not 0:
                rule = Rule()
                rule.name = row[0]
                rule.temp_min = parse_float(row[1])
                rule.temp_max = parse_float(row[2])
                rule.tone_min = parse_int(row[3])
                rule.tone_max = parse_int(row[4])
                rule.hum_min = parse_float(row[5])
                rule.hum_max = parse_float(row[6])
                rule.pm25_min = parse_float(row[7])
                rule.pm25_max = parse_float(row[8])
                rule.pm10_min = parse_float(row[9])
                rule.pm10_max = parse_float(row[10])
                rule.button_active = parse_bool(row[11])
                rule.printer_state = parse_str(row[12])

                rule.outlet_1 = parse_bool(row[13])
                rule.outlet_2 = parse_bool(row[14])
                rule.outlet_3 = parse_bool(row[15])
                rule.outlet_4 = parse_bool(row[16])
                print(rule)
                rules.append(rule)
            line_count = +1


def find(temp, tone, hum, pm25, pm10, button_active, printer_state):
    global last_rule
    print(f"Searching for rule with temp: {temp}, tone: {tone}, hum: {hum}, pm2.5: {pm25}, pm10: {pm10}, button_active: {button_active}, printer_state: {printer_state}")
    for rule in rules:
        if rule.applies(temp, tone, hum, pm25, pm10, button_active, printer_state) and last_rule is not rule:
            last_rule = rule
            return rule
        else:
            return None


def parse_str(val):
    val = val.strip()
    if val == "-":
        return None
    return val.lower()


def parse_float(val):
    val = val.strip()
    if val == "-":
        return None
    return float(val)


def parse_int(val):
    val = val.strip()
    if val == "-":
        return None
    return int(val)


def parse_bool(val):
    val = val.strip()
    if val == "-":
        return None
    return val == "0" if True else False


class Rule:
    temp_min: float
    temp_max: float
    tone_min: int
    tone_max: int
    hum_min: float
    hum_max: float
    pm25_min: float
    pm25_max: float
    pm10_min: float
    pm10_max: float
    button_active: bool
    printer_state: str

    outlet_1: bool
    outlet_2: bool
    outlet_3: bool
    outlet_4: bool
    printer_run: bool

    def applies(self, temp, tone, hum, pm25, pm10, button_active, printer_state):
        valid = True
        if self.temp_min is not None and self.temp_max is not None:
            if self.temp_min >= temp or temp >= self.temp_max:
                valid = False
        if self.tone_min is not None and self.tone_max is not None:
            if self.tone_min >= tone or tone >= self.tone_max:
                valid = False
        if self.hum_min is not None and self.hum_max is not None:
            if self.hum_min >= hum or hum >= self.hum_max:
                valid = False

        if self.pm25_min is not None and self.pm25_max is not None:
            if self.pm25_min >= pm25 or pm25 >= self.pm25_max:
                valid = False
        if self.pm10_min is not None and self.pm10_max is not None:
            if self.pm10_min >= pm10 or pm10 >= self.pm10_max:
                valid = False

        if self.button_active is not None:
            if self.button_active != button_active:
                valid = False
        if self.printer_state is not None:
            if self.printer_state != printer_state:
                valid = False

        return valid

    def __str__(self):
        return json.dumps(self.__dict__)

