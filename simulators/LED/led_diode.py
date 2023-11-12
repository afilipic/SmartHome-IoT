
import time

import keyboard as keyboard


def generate_values_sensors():
    light_state = "OFF"
    while True:
        if keyboard.is_pressed('x'):
            light_state = "ON"
        if keyboard.is_pressed('y'):
            light_state = "OFF"
        yield light_state

def run_dl_simulator(delay,name, callback, stop_event):
    # Simulate some status code, e.g., 0 for success
    code = 0
    i = 0
    for s in generate_values_sensors():
        time.sleep(delay)  # Delay between readings
        # Now pass the code as well, assuming code=0 means success
        callback(s, name)
        i += 1
        if stop_event.is_set() or i == 5:
            break
