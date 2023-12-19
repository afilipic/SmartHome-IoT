# import time
# import threading
#
# from sensors.UDS.DUS1 import run_dus_loop
# from simulators.UDS.uds import run_dus_simulator
#
# def door_ultrasonic_sensor_callback(distance, print_lock):
#     t = time.localtime()
#     print("\n--------UDS----------------------------------")
#     print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
#     print("-" * 45)
#     print("Distance from the door is: " + str(distance) + " centimeters.")
#     print("-" * 45 + "\n")
#
# def run_DUS(settings, threads, stop_event,lock):
#     if settings['simulated']:
#         door_ultrasonic_sensor_thread = threading.Thread(target = run_dus_simulator, args=(2, door_ultrasonic_sensor_callback, stop_event,lock))
#         door_ultrasonic_sensor_thread.start()
#         threads.append(door_ultrasonic_sensor_thread)
#         print(f"DUS sensor simulation started")
#     else:
#         door_ultrasonic_sensor_pin = settings['pin']
#         door_ultrasonic_sensor_thread = threading.Thread(target = run_dus_loop, args=(2, door_ultrasonic_sensor_callback, stop_event))
#         door_ultrasonic_sensor_thread.start()
#         threads.append(door_ultrasonic_sensor_thread)
#         print(f"DUS loop started")

from simulators.UDS.uds import run_dus_simulator
from sensors.UDS.DUS1 import run_dus_loop
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


def dus_callback(stop_event, dus_settings, publish_event, distance):
    global publish_data_counter, publish_data_limit


    code_payload = {

        "measurement": "Distance",
        "simulated": dus_settings['simulated'],
        "runs_on": dus_settings["runs_on"],
        "name": dus_settings["name"],
        "value": distance
    }

    with counter_lock:
        dus_batch.append(('Distance', json.dumps(code_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()


def run_dus(settings, threads, stop_event):
    if settings['simulated']:
        print("Starting dus sumilator")
        dus_thread = threading.Thread(target = run_dus_simulator, args=(2, dus_callback, stop_event, publish_event, settings))
        dus_thread.start()
        threads.append(dus_thread)
        print("Dht1 sumilator started")
    else:
        print("Starting dus loop")
        dus_thread = threading.Thread(target=run_dus_loop, args=(2, dus_callback, stop_event, publish_event, settings))
        dus_thread.start()
        threads.append(dus_thread)
        print("Dms loop started")