import threading
from simulators.MS.dms import simulated_dms


def run_dms(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting keypad simulator")
        keypad_thread = threading.Thread(target=simulated_dms, args=(2,stop_event))
        keypad_thread.start()
        threads.append(keypad_thread)
    else:
        print("Starting real keypad")
        keypad_thread = threading.Thread(target=simulated_dms, args=(stop_event,))
        keypad_thread.start()
        threads.append(keypad_thread)