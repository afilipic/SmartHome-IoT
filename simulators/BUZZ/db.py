import threading
import time
import keyboard
try:
    import winsound
    importedWinsound = True
except:
    importedWinsound = False
    pass


def run_db_simulator(setting,publish_event,callback,stop_event, pitch, duration):
    print(f"Press b to activate the simulated buzzer or q to quit.")
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("b"):
            print("Door buzzer activated!")
            if(importedWinsound):
                #winsound.Beep(pitch, duration)
                callback(publish_event,setting)
            time.sleep(1)
