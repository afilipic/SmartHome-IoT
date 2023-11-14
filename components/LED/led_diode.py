import threading
import time

from sensors.LED.DL import run_dl_loop
from simulators.LED.led_diode import run_dl_simulator


def dl_callback(state, print_lock, dl):
    with print_lock:
        t = time.localtime()
        print("\n-------LED---------")
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print("-" * 20)
        print(f"State: {state}")
        print("-" * 20 + "\n")


def run_dl(settings, threads, stop_event):
    if settings['simulated']:
        dl_pin = settings['pin']
        dl_thread = threading.Thread(target=run_dl_simulator, args=(dl_callback, stop_event))
        dl_thread.start()
        threads.append(dl_thread)
        print("Dl sumilator started")
    else:
        dl_pin = settings['pin']
        button_pin = settings['button_pin']
        dl_thread = threading.Thread(target=run_dl_loop, args=(button_pin, dl_pin, dl_callback, stop_event))
        dl_thread.start()
        threads.append(dl_thread)
        print("Dl loop started")