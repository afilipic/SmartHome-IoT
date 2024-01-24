from simulators.PI1.UDS.uds import run_dus_simulator
from sensors.PI1.UDS.DUS1 import run_dus_loop
import threading
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT

dus_batch = []
publish_data_counter = 0
publish_data_limit = 5
counter_lock = threading.Lock()


def publisher_task(event, dus_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_dus_batch = dus_batch.copy()
            publish_data_counter = 0
            dus_batch.clear()
        publish.multiple(local_dus_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} dus values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dus_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def dus_callback(stop_event, dus_settings, publish_event, distance,number_of_people):
    global publish_data_counter, publish_data_limit


    code_payload = {

        "measurement": "Distance",
        "simulated": dus_settings['simulated'],
        "runs_on": dus_settings["runs_on"],
        "name": dus_settings["name"],
        "value": distance
    }
    nop_payload = {

        "measurement": "Number of people",
        "simulated": dus_settings['simulated'],
        "runs_on": dus_settings["runs_on"],
        "name": dus_settings["name"],
        "value": number_of_people
    }

    with counter_lock:
        dus_batch.append(('Distance', json.dumps(code_payload), 0, True))
        dus_batch.append(('Number of people', json.dumps(nop_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()


def run_dus(settings, threads, stop_event,lock,number_of_people_thread,home):
    if settings['simulated']:
        print("Starting dus sumilator")
        dus_thread = threading.Thread(target = run_dus_simulator, args=(2, dus_callback, stop_event, publish_event, settings,lock,number_of_people_thread,home))
        dus_thread.start()
        threads.append(dus_thread)
        print("Dus sumilator started")
    else:
        print("Starting dus loop")
        dus_thread = threading.Thread(target=run_dus_loop, args=(2, dus_callback, stop_event, publish_event, settings))
        dus_thread.start()
        threads.append(dus_thread)
        print("Dus loop started")