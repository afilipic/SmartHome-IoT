import threading
import time
import keyboard
try:
    import winsound
except:
    pass


def listen_for_keypress(stop_event, print_lock,pitch, duration):
    print(f"Press b to activate the simulated buzzer or q to quit.")
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("b"):
            winsound.Beep(pitch, duration)
            print("Door buzzer activated!")
            time.sleep(1)
