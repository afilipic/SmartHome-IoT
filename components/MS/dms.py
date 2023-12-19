from simulators.MS.dms import run_dms_simulator
from sensors.MS.DMS import run_dms_loop
import threading
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT


dms_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()


def publisher_task(event, ms_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_ms_batch = ms_batch.copy()
            publish_data_counter = 0
            ms_batch.clear()
        publish.multiple(local_ms_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} ms values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dms_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def dms_callback(stop_event, dms_settings, publish_event, code):
    global publish_data_counter, publish_data_limit


    code_payload = {
        "measurement": "Keypads",
        "simulated": dms_settings['simulated'],
        "runs_on": dms_settings["runs_on"],
        "name": dms_settings["name"],
        "value": code
    }

    with counter_lock:
        dms_batch.append(('Keypads', json.dumps(code_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()


def run_dms(settings, threads, stop_event,lock):
    if settings['simulated']:
        print("Starting dms sumilator")
        dms_thread = threading.Thread(target = run_dms_simulator, args=(2, dms_callback, stop_event, publish_event, settings,lock))
        dms_thread.start()
        threads.append(dms_thread)
        print("Dht1 sumilator started")
    else:
        print("Starting dms loop")
        dms_thread = threading.Thread(target=run_dms_loop, args=(2, dms_callback, stop_event, publish_event, settings))
        dms_thread.start()
        threads.append(dms_thread)
        print("Dms loop started")
