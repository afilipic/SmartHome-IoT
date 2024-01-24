import time
import random

def generate_random_color():
    colors = {
        0: "Off",
        1: "White",
        2: "Red",
        3: "Green",
        4: "Blue",
        5: "Yellow",
        6: "Purple",
        7: "Light Blue"
    }
    return random.choice(list(colors.items()))

def run_brgb_simulator(settings,publish_event,brgb_callback,stop_event):
    while not stop_event.is_set():
        time.sleep(1)
        color_value, color_name = generate_random_color()
        brgb_callback(publish_event, settings,color_name)

