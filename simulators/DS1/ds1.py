import time
import random

def generate_values_door_sensor():
    while True:
        state = random.randint(0, 1)
        if state < 0:
            state = 0
        if state > 1:
            state = 1
        yield state


def run_ds1_simulator(delay, callback, stop_event):
    # Simulate some status code, e.g., 0 for success
    code = 0
    i = 0
    for s in generate_values_door_sensor():
        time.sleep(delay)  # Delay between readings
        # Now pass the code as well, assuming code=0 means success
        callback(s, code)
        i += 1
        if stop_event.is_set() or i == 5:
            break