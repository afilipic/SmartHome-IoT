import time
import threading

from sensors.PIR.DPIR1 import run_dpir_loop
from sensors.PIR.DS1 import run_ds_loop
from sensors.PIR.RPIR1 import run_rpir1_loop
from sensors.PIR.RPIR2 import run_rpir2_loop
from simulators.PIR.pir import run_pir_simulator

def door_sensor_callback(state,name):
    t = time.localtime()
    print("\n-------"+name+"----------")
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print("-" * 20)
    if(state == 1):
        print(name + "sensor is detecting something")
    if(state == 0):
        print(name + "sensor is detecting nothing")
    print("-" * 20 + "\n")

def run_DS1(settings, threads, stop_event):
    name = "Door "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DS1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_ds_loop, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DS1 sensor loop started")

def run_DPIR1(settings, threads, stop_event):
    name = "Door motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_dpir_loop, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR1 sensor loop started")

def run_RPIR1(settings, threads, stop_event):
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir1_loop, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR1 sensor loop started")

def run_RPIR2(settings, threads, stop_event):
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR2 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir2_loop, args=(2, name, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR2 sensor loop started")