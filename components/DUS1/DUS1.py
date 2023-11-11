import time
import threading
from simulators.DUS1.DUS1 import run_dus1_simulator

def door_ultrasonic_sensor_callback(distance, print_lock):
    t = time.localtime()
    print("-"*20)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print("-" * 20)
    print("Distance from the door is: " + str(distance) + " centimeters.")

def run_ultrasonic_door_sensor(settings, threads, stop_event):
    if settings['simulated']:
        door_ultrasonic_sensor_thread = threading.Thread(target = run_dus1_simulator, args=(2, door_ultrasonic_sensor_callback, stop_event))
        door_ultrasonic_sensor_thread.start()
        threads.append(door_ultrasonic_sensor_thread)
        print(f"Door Sensor simulation started")
    else:
        door_ultrasonic_sensor_pin = settings['pin']
        door_ultrasonic_sensor_thread = threading.Thread(target = run_dus1_simulator, args=(2, door_ultrasonic_sensor_callback, stop_event))
        door_ultrasonic_sensor_thread.start()
        threads.append(door_ultrasonic_sensor_thread)
        print(f"Door Sensor loop started")