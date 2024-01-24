import threading
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
from simulators.PI1.PIR.pir import run_pir_simulator
from sensors.PI1.PIR.RPIR1 import run_rpir1_loop
from sensors.PI1.PIR.RPIR2 import run_rpir2_loop
from sensors.PI1.PIR.DPIR1 import run_dpir_loop


pir_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()
from sensors.PI1.PIR.DS1 import run_ds_loop


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


def door_sensor_callback(state, publish_event, pir_settings,light_event,number_of_people_thread,alarm=False, code="PIRLIB_OK", verbose=False):
    global publish_data_counter, publish_data_limit

    if verbose:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print(f"value: {state}")

    temp_payload = {
        "measurement": "sensor",
        "simulated": pir_settings['simulated'],
        "runs_on": pir_settings["runs_on"],
        "name": pir_settings["name"],
        "value": state,
        "alarm": alarm
    }

    if state and light_event:
        light_event.set()

    with counter_lock:
        pir_batch.append(("Sensor", json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

def run_DPIR1(settings, threads, stop_event,lock,light_event,number_of_people_thread):
    sensor = "DPIR1"
    name = "Door motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock,light_event,number_of_people_thread))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_dpir_loop, args=(settings, door_sensor_callback,publish_event, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR1 sensor loop started")

def run_DPIR2(settings, threads, stop_event,lock,light_event,number_of_people_thread):
    sensor = "DPIR2"
    name = "Door motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock,light_event,number_of_people_thread))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR2 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_dpir_loop, args=(settings, door_sensor_callback,publish_event, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"DPIR2 sensor loop started")

def run_RPIR1(settings, threads, stop_event,lock,home):
    sensor = "RPIR1"
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock,None,None,home))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR1 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir1_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR1 sensor loop started")

def run_RPIR2(settings, threads, stop_event,lock,home):
    sensor = "RPIR2"
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock,None,None,home))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR2 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir2_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR2 sensor loop started")


def run_RPIR3(settings, threads, stop_event,lock,home):
    sensor = "RPIR3"
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock,None,None,home))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR3 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir2_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR3 sensor loop started")

def run_RPIR4(settings, threads, stop_event,lock,home):
    sensor = "RPIR4"
    name = "Room motion "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_pir_simulator, args=(settings,publish_event, door_sensor_callback, stop_event,lock,None,None,home))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR4 sensor simulation started")
    else:
        door_pin = settings['pin']
        door_sensor_thread = threading.Thread(target = run_rpir2_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"RPIR4 sensor loop started")