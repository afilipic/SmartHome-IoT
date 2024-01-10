import threading

from sensors.PI3.B4SD.b4sd import run_b4sd_loop
from simulators.PI1.BUZZ.db import run_db_simulator
from sensors.PI1.BUZZ.DB import run_buzzer_loop
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
from simulators.PI3.B4SD.b4sd import run_b4sd_simulator

b4sd_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()


def publisher_task(event, db_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_db_batch = db_batch.copy()
            publish_data_counter = 0
            db_batch.clear()
        publish.multiple(local_db_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} b4sd values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, b4sd_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def b4sd_callback(publish_event, b4sd_settings,value):
    global publish_data_counter, publish_data_limit

    temp_payload = {
        "measurement": "Time",
        "simulated": b4sd_settings['simulated'],
        "runs_on": b4sd_settings["runs_on"],
        "name": b4sd_settings["name"],
        "value": value
    }

    with counter_lock:
        b4sd_batch.append(("Time", json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

def run_b4sd(settings, threads, stop_event,lock):
    pitch = settings.get('pitch', 440)
    duration = settings.get('duration', 1)

    if settings['simulated']:
        print("Starting B4SD simulator")
        buzzer_thread = threading.Thread(target=run_b4sd_simulator, args=(settings,publish_event,b4sd_callback,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("B4SD simulator started")
    else:
        print("Starting real B4SD")
        buzzer_pin = settings['pin']
        buzzer_thread = threading.Thread(target=run_b4sd_loop, args=(buzzer_pin, 2, 2,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("Real B4SD started")
