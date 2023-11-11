import time
import threading
from simulators.PIR.pir import run_pir_simulator

def door_sensor_callback(state,name):
    t = time.localtime()
    print("-"*20)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print("-" * 20)
    if(state == 1):
        print(name + "sensor is detecting something")
    if(state == 0):
        print(name + "sensor is detecting nothing")

def run_door_sensor(settings, threads, stop_event):
    name = "Door "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Door sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Door sensor loop started")

def run_DPIR1(settings, threads, stop_event):
    name = "Door motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Door motion sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Door motion sensor loop started")

def run_RPIR1(settings, threads, stop_event):
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Room motion sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Room motion sensor loop started")

def run_RPIR2(settings, threads, stop_event):
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Room motion sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Room motion sensor loop started")