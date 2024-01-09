import threading
from simulators.BUZZ.db import run_db_simulator
from sensors.BUZZ.DB import run_buzzer_loop
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT


db_batch = []
publish_data_counter = 0
publish_data_limit = 1
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
        print(f'published {publish_data_limit} db values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, db_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def door_buzzer_callback(publish_event, db_settings, code="DBLIB_OK", verbose=False):
    global publish_data_counter, publish_data_limit

    if verbose:
        t = time.localtime()
        print("="*20)
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print(f"Code: {code}")
        print(f"Buzzer: 2s")

    temp_payload = {
        "measurement": "Door Buzzer",
        "simulated": db_settings['simulated'],
        "runs_on": db_settings["runs_on"],
        "name": db_settings["name"],
        "value": 1
    }

    with counter_lock:
        db_batch.append(("Door Buzzer", json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

def run_door_buzzer(settings, threads, stop_event):
    pitch = settings.get('pitch', 440)
    duration = settings.get('duration', 1)

    if settings['simulated']:
        print("Starting door buzzer simulator")
        buzzer_thread = threading.Thread(target=run_db_simulator, args=(settings,publish_event,door_buzzer_callback,stop_event, pitch, duration))
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
