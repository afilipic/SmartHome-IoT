import time
import random

def generate_values_door_sensor(initial_state=400):
    distance = initial_state
    while True:
        distance = distance + random.randint(-50, 50)
        if distance < 0:
            distance = 0
        if distance > 400:
            distance = 400
        yield distance


def run_dus_simulator(delay, callback, stop_event,lock):
    while True:
        code = 0
        i = 0
        for d in generate_values_door_sensor():
            time.sleep(delay)
            with lock:
                callback(d, code)
            i += 1
            if stop_event.is_set():
                break