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


def run_pir_simulator(delay,name,sensor, callback, stop_event,lock):
    while True:
        code = 0
        i = 0
        for s in generate_values_sensors():
            time.sleep(delay)
            with lock:
                callback(s,name,sensor)
            i += 1
            if stop_event.is_set():
                break

