import threading

from sensors.PI3.BIR.bir import run_bir_loop
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT
from simulators.PI3.B4SD.b4sd import run_b4sd_simulator
from simulators.PI3.BIR.bir import run_bir_simulator
from simulators.PI3.BRGB.brgb import run_brgb_simulator

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
        print(f'published {publish_data_limit} brgb values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, b4sd_batch,))
publisher_thread.daemon = True
publisher_thread.start()


def brgb_callback(publish_event, brgb_settings,value):
    global publish_data_counter, publish_data_limit

    temp_payload = {
        "measurement": "BRGB",
        "simulated": brgb_settings['simulated'],
        "runs_on": brgb_settings["runs_on"],
        "name": brgb_settings["name"],
        "value": value
    }

    with counter_lock:
        b4sd_batch.append(("BRGB", json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

def run_brgb(settings, threads, stop_event,lock):
    pitch = settings.get('pitch', 440)
    duration = settings.get('duration', 1)

    if settings['simulated']:
        print("Starting BRGB simulator")
        buzzer_thread = threading.Thread(target=run_brgb_simulator, args=(settings,publish_event,brgb_callback,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("BRGB simulator started")
    else:
        print("Starting real BRGB")
        buzzer_pin = settings['pin']
        buzzer_thread = threading.Thread(target=run_bir_loop, args=(buzzer_pin, 2, 2,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("Real BRGB started")
