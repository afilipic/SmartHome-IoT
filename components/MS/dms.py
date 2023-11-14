import threading

from sensors.MS.DMS import run_dms_loop
from simulators.MS.dms import run_dms_simulator


def run_dms(settings, threads, stop_event):
    if settings['simulated']:
        print("DMS sensor simulation started")
        keypad_thread = threading.Thread(target=run_dms_simulator, args=(2, stop_event))
        keypad_thread.start()
        threads.append(keypad_thread)
    else:
        print("Starting real keypad")
        keypad_thread = threading.Thread(target=run_dms_loop, args=(stop_event,))
        keypad_thread.start()
        threads.append(keypad_thread)