import threading
import time

from simulators.LED.led_diode import run_dl_simulator


def dl_callback(state, print_lock, dl):
    with print_lock:
        t = time.localtime()
        print("=" * 20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"State: {state}")


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
        dl_thread = threading.Thread(target=run_dl_simulator, args=(button_pin, dl_pin, dl_callback, stop_event))
        dl_thread.start()
        threads.append(dl_thread)
        print("Dl loop started")