import time
import random

Options= ["UP", "DOWN", "2", "3", "1", "4", "5", "6", "7"]

def generate_values():
    while True:
        yield random.choice(Options)
        time.sleep(1)


def run_bir_simulator(settings, publish_event, bir_callback, stop_event,rgb_queue):
    for button in generate_values():
        if stop_event.is_set():
            break
        if rgb_queue:
            rgb_queue.put(button)

        bir_callback(publish_event,settings, button)

