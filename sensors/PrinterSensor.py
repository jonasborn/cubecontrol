from octorest import OctoRest

import config.Config

state = "offline"
client: OctoRest


def init():
    global client
    client = OctoRest(url=config.Config.printer_url, apikey=config.Config.printer_key)


def __main_loop():
    global state
    state = client.job_info()["state"].lower()
