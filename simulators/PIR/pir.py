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


def run_pir_simulator(settings,publish_event, callback, stop_event,lock):
    delay = 2
    while not stop_event.is_set():
        code = 0
        i = 0
        for s in generate_values_sensors():
            time.sleep(delay)
            with lock:
                callback(s,publish_event,settings)#state, publish_event, pir_settings,
            i += 1


