
import time

import keyboard as keyboard


def run_dl_simulator(callback, stop_event):
    print("Press x to turn on light, y to turn off the light or q to quit.")
    light_state = "OFF"
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("x") and light_state == "ON":
            print("Light is already on!")
            time.sleep(0.2)
        elif keyboard.is_pressed("x") and light_state == "OFF":
            light_state = "ON"
            print("Light is now on!")
            time.sleep(0.2)
        elif keyboard.is_pressed("y") and light_state == "OFF":
            print("Light is already off!")
            time.sleep(0.2)
        elif keyboard.is_pressed("y") and light_state == "ON":
            light_state = "OFF"
            print("Light is now off!")
            time.sleep(0.2)
