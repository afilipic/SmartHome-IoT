import threading
import time
import json
import paho.mqtt.publish as publish
from simulators.PI1.GYRO.gyro import run_gyroscope_simulator
from broker_settings import HOSTNAME, PORT


gyro_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()


def publisher_task(event, gyro_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_gyro_batch = gyro_batch.copy()
            publish_data_counter = 0
            gyro_batch.clear()
        publish.multiple(local_gyro_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} gyro values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, gyro_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def gyro_callback( temperature, publish_event, dht_settings, code="GYROLIB_OK", verbose=False):
    global publish_data_counter, publish_data_limit

    temp_payload = {
        "measurement": "GYRO",
        "simulated": dht_settings['simulated'],
        "runs_on": dht_settings["runs_on"],
        "name": dht_settings["name"],
        "value": temperature
    }

    with counter_lock:
        gyro_batch.append(('GYRO', json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()


def run_gyro(settings, threads, stop_event,lock):
    sensor = "Gyroscope"
    name = "Gyroscope "
    if settings['simulated']:
        door_sensor_thread = threading.Thread(target = run_gyroscope_simulator, args=(settings,publish_event, gyro_callback, stop_event,lock))
        door_sensor_thread.start()
        threads.append(door_sensor_thread)
        print(f"Gyroscope sensor simulation started")
    else:
        door_pin = settings['pin']
        #door_sensor_thread = threading.Thread(target = run_ds_loop, args=(settings,publish_event, door_sensor_callback, stop_event))
        #door_sensor_thread.start()
        #threads.append(door_sensor_thread)
        print(f"DS1 sensor loop started")