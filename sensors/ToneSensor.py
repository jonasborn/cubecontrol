import logging

import sounddevice as sd
import numpy as np
import scipy.fftpack
import config.Config
import _thread

# General settings
__SAMPLE_FREQ = config.Config.alarm_sampling_rate  # sample frequency in Hz
__WINDOW_SIZE = config.Config.alarm_sampling_rate  # window size of the DFT in samples
__WINDOW_STEP = 21050  # step size of window
__WINDOW_T_LEN = __WINDOW_SIZE / __SAMPLE_FREQ  # length of the window in seconds
__SAMPLE_T_LENGTH = 1 / __SAMPLE_FREQ  # length between two samples in seconds
__window_samples = [0 for _ in range(__WINDOW_SIZE)]

__CONCERT_PITCH = 440

tone: int = 0


def current_tone():
    global tone
    return tone


def init():
    _thread.start_new_thread(__main_loop, ())

def show():
    print("Showing current audio devices available:")
    for dev in sd.query_devices():
        print("Name: " + dev["name"] + ", Rate: " + str(dev["default_samplerate"]))

def __main_loop():
    global __SAMPLE_FREQ, __WINDOW_SIZE, __WINDOW_STEP

    try:
        with sd.InputStream(channels=1, callback=callback, device=config.Config.alarm_device,
                            blocksize=__WINDOW_STEP,
                            samplerate=__SAMPLE_FREQ):
            while True:
                pass
    except Exception as e:
        logging.error("Unable to open audio device called " + config.Config.alarm_device)
        print(str(e))


# The sounddecive callback function
# Provides us with new data once WINDOW_STEP samples have been fetched
def callback(indata, frames, time, status):
    global __window_samples, tone
    if status:
        print(status)
    if any(indata):
        __window_samples = np.concatenate((__window_samples, indata[:, 0]))  # append new samples
        __window_samples = __window_samples[len(indata[:, 0]):]  # remove old samples
        magnitude_spec = abs(scipy.fftpack.fft(__window_samples)[:len(__window_samples) // 2])

        for i in range(int(62 / (__SAMPLE_FREQ / __WINDOW_SIZE))):
            magnitude_spec[i] = 0  # suppress mains hum

        maxInd = np.argmax(magnitude_spec)
        maxFreq = maxInd * (__SAMPLE_FREQ / __WINDOW_SIZE)

        tone = maxFreq

    else:
        print('no input')
