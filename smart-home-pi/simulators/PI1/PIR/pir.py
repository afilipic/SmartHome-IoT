import time
import random

def generate_values_sensors(settings):
    while True:
        state = random.randint(0, 1)
        if state < 0:
            state = False
            print(settings["name"]," sensor detected no movement")
        if state > 1:
            state = True
            print(settings["name"]," sensor detected movement")
        yield state


def run_pir_simulator(settings,publish_event, callback, stop_event,lock,light_event=None):
    delay = 2
    while not stop_event.is_set():
        i = 0
        for s in generate_values_sensors(settings):
            time.sleep(delay)
            with lock:
                callback(s,publish_event,settings,light_event)
            i += 1


