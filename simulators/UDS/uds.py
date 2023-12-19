import time
import random

def generate_values_door_sensor(initial_state=400):
    # distance = initial_state
    # while True:
    #     distance = distance + random.randint(-50, 50)
    #     if distance < 0:
    #         distance = 0
    #     if distance > 400:
    #         distance = 400
    #     yield distance
    distance = random.randint(0, 400)
    while True:
        distance = distance + random.randint(-50, 50)
        if distance < 0 or distance > 400:
            distance = random.randint(0, 400)
            yield 0

        yield distance


def run_dus_simulator(delay,dus_callback, stop_event, publish_event, settings):
    while not stop_event.is_set():
        for d in generate_values_door_sensor():
            time.sleep(delay)
            dus_callback(stop_event, settings, publish_event, d)
