import time
import threading

from sensors.UDS.DUS1 import run_dus_loop
from simulators.UDS.uds import run_dus_simulator

def door_ultrasonic_sensor_callback(distance, print_lock):
    t = time.localtime()
    #print("\n--------UDS----------------------------------")
    #print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    #print("-" * 45)
    #print("Distance from the door is: " + str(distance) + " centimeters.")
    #qprint("-" * 45 + "\n")

def run_DUS(settings, threads, stop_event,lock):
    if settings['simulated']:
        door_ultrasonic_sensor_thread = threading.Thread(target = run_dus_simulator, args=(2, door_ultrasonic_sensor_callback, stop_event,lock))
        door_ultrasonic_sensor_thread.start()
        threads.append(door_ultrasonic_sensor_thread)
        print(f"DUS sensor simulation started")
    else:
        door_ultrasonic_sensor_pin = settings['pin']
        door_ultrasonic_sensor_thread = threading.Thread(target = run_dus_loop, args=(2, door_ultrasonic_sensor_callback, stop_event))
        door_ultrasonic_sensor_thread.start()
        threads.append(door_ultrasonic_sensor_thread)
        print(f"DUS loop started")