import time
import keyboard

def run_dl_simulator(settings, publish_event, dl_callback, stop_event):
    print("Press 'l' to toggle the LED state or 'q' to quit.")
    while not stop_event.is_set():
        if keyboard.is_pressed('l'):
            print("Led activated!")
            dl_callback(publish_event, settings)
            time.sleep(0.5)  # Debounce delay
        elif keyboard.is_pressed('q'):
            print("Quitting LED simulator...")
            stop_event.set()
        time.sleep(0.1)
