import threading
import time
import keyboard
try:
    import winsound
except:
    pass


def \
        run_db_simulator(stop_event, print_lock, pitch, duration):
    print(f"Press b to activate the simulated buzzer or q to quit.")
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("b"):
            print("Door buzzer activated!")
            winsound.Beep(pitch, duration)
            time.sleep(1)
