'''
import time
import threading

from sensors.PIR.DPIR1 import run_dpir_loop
from sensors.PIR.DS1 import run_ds_loop
from sensors.PIR.RPIR1 import run_rpir1_loop
from sensors.PIR.RPIR2 import run_rpir2_loop
from simulators.PIR.pir import run_pir_simulator

def door_sensor_callback(state,name,sensor):
    t = time.localtime()
    print("\n--------"+sensor+"--------------------------------")
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print("-" * 45 )
    if(state == 1):
        print(name + "sensor is detecting something")
    if(state == 0):
        print(name + "sensor is detecting nothing")
    print("-" * 45 + "\n")
'''
from simulators.DHT.dht import run_dht_simulator
import threading
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
from simulators.PIR.pir import run_pir_simulator
from sensors.PIR.RPIR1 import run_rpir1_loop
from sensors.PIR.RPIR2 import run_rpir2_loop
from sensors.PIR.DPIR1 import run_dpir_loop


pir_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()
from sensors.PIR.DS1 import run_ds_loop


def publisher_task(event, pir_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_ds1_batch = pir_batch.copy()
            publish_data_counter = 0
            pir_batch.clear()
        publish.multiple(local_ds1_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} pir values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, pir_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def door_sensor_callback(state, publish_event, pir_settings, code="PIRLIB_OK", verbose=False):
    global publish_data_counter, publish_data_limit

    if verbose:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print(f"value: {state}")

    temp_payload = {
        "measurement": "Sensor",
        "simulated": pir_settings['simulated'],
        "runs_on": pir_settings["runs_on"],
        "name": pir_settings["name"],
        "value": state
    }

    with counter_lock:
        pir_batch.append(("Sensor " +pir_settings["name"], json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

def run_DS1(settings, threads, stop_event,lock):
    sensor = "DS1"
    name = "Door "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DS1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_ds_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DS1 sensor loop started")

def run_DPIR1(settings, threads, stop_event,lock):
    sensor = "DPIR1"
    name = "Door motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_dpir_loop, args=(settings, door_sensor_callback,publish_event, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR1 sensor loop started")

def run_RPIR1(settings, threads, stop_event,lock):
    sensor = "RPIR1"
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir1_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR1 sensor loop started")

def run_RPIR2(settings, threads, stop_event,lock):
    sensor = "RPIR2"
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR2 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir2_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR2 sensor loop started")