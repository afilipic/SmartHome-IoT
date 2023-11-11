import time
import threading
from simulators.DS1.ds1 import run_ds1_simulator

def door_sensor_callback(state, print_lock):
    t = time.localtime()
    print("-"*20)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print("-" * 20)
    if(state == 1):
        print("Door sensor is detecting something")
    if(state == 0):
        print("Door sensor is detecting nothing")

def run_door_sensor(settings, threads, stop_event):
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_ds1_simulator, args=(2, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Door Sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_ds1_simulator, args=(2, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Door Sensor loop started")