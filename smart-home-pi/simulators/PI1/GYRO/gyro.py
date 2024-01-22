import time
import random

def generate_values_sensors():
    while True:
        state = random.randint(0, 10)
        if state > 7:
            state = 1
        else:
            state = 0
        yield state


def run_gyroscope_simulator(settings,publish_event, callback, stop_event,lock):
    delay = 2
    while not stop_event.is_set():
        i = 0
        for s in generate_values_sensors():
            time.sleep(delay)
            with lock:
                callback(s,publish_event,settings)
            i += 1

