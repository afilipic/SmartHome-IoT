import threading
from simulators.BUZZ.db import run_db_simulator
from sensors.BUZZ.DB import run_buzzer_loop

def run_door_buzzer(settings, threads, stop_event,print_lock):
    pitch = settings.get('pitch', 440)
    duration = settings.get('duration', 1)

    if settings['simulated']:
        print("Starting door buzzer simulator")
        buzzer_thread = threading.Thread(target=run_db_simulator, args=(stop_event, print_lock, pitch, duration))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("Buzzer simulator started")
    else:
        print("Starting real door buzzer")
        buzzer_pin = settings['pin']
        buzzer_thread = threading.Thread(target=run_buzzer_loop, args=(buzzer_pin, 2, 2,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("Real buzzer started")
