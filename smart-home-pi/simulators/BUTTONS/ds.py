import threading
import time
import keyboard


def run_ds_simulator(setting, publish_event, callback, stop_event):
    print(f"Press 's' to activate the simulated sensor or 'q' to quit.")
    aktivacija_alarma = 0

    while not stop_event.is_set():
        if keyboard.is_pressed("q"):
            stop_event.set()
            break
        if keyboard.is_pressed("s"):
            callback(publish_event, setting, 1)
            print("Door sensor activated!")
            time.sleep(1)
            aktivacija_alarma += 1
            if aktivacija_alarma >= 5:
                print("Alarm is activated, evacuate!")
        else:
            callback(publish_event, setting, 0)
            print("Door sensor not activated!")
            time.sleep(1)
            aktivacija_alarma = 0

    print("Simulator stopped.")
