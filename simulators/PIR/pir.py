import time
import random

def generate_values_sensors():
    while True:
        state = random.randint(0, 1)
        if state < 0:
            state = 0
        if state > 1:
            state = 1
        yield state


def run_pir_simulator(delay,name, callback, stop_event):
    # Simulate some status code, e.g., 0 for success
    code = 0
    i = 0
    for s in generate_values_sensors():
        time.sleep(delay)  # Delay between readings
        # Now pass the code as well, assuming code=0 means success
        callback(s,name)
        i += 1
        if stop_event.is_set():
            break

