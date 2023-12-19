import time
import random

def run_dms_simulator( delay,dms_callback, stop_event, publish_event, settings):

    while True:
        if stop_event.is_set():
            break
        valid_values = {"1", "2", "3", "A", "4", "5", "6", "B", "7", "8", "9", "C", "*", "0", "D"}
        sensored_values = []

        for _ in range(5):
            simulated_key_press = random.choice(list(valid_values))
            sensored_values.append(simulated_key_press)
            time.sleep(delay)
        sensored_values.append('#')

        if sensored_values:

            code = ", ".join(sensored_values)
            dms_callback(stop_event, settings, publish_event, code)