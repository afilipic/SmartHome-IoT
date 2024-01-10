import threading
from simulators.PI1.LED.led_diode import run_dl_simulator
from sensors.PI1.LED.DL import run_dl_loop
import time
import json
import paho.mqtt.publish as publish
from broker_settings import HOSTNAME, PORT


dl_batch = []
publish_data_counter = 0
publish_data_limit = 1
counter_lock = threading.Lock()


def publisher_task(event, dl_batch):
    global publish_data_counter, publish_data_limit
    while True:
        event.wait()
        with counter_lock:
            local_dl_batch = dl_batch.copy()
            publish_data_counter = 0
            dl_batch.clear()
        publish.multiple(local_dl_batch, hostname=HOSTNAME, port=PORT)
        print(f'published {publish_data_limit} dl values')
        event.clear()


publish_event = threading.Event()
publisher_thread = threading.Thread(target=publisher_task, args=(publish_event, dl_batch,))
publisher_thread.daemon = True
publisher_thread.start()

led_state = 0
def dl_callback(publish_event, dl_settings):
    global publish_data_counter, publish_data_limit, led_state

    led_state = 1 - led_state
    temp_payload = {
        "measurement": "Led Diode",
        "simulated": dl_settings['simulated'],
        "runs_on": dl_settings["runs_on"],
        "name": dl_settings["name"],
        "value": led_state
    }

    with counter_lock:
        dl_batch.append(("Led Diode", json.dumps(temp_payload), 0, True))
        publish_data_counter += 1

    if publish_data_counter >= publish_data_limit:
        publish_event.set()

def run_dl(settings, threads, stop_event):

    if settings['simulated']:
        print("Starting led diode simulator")
        buzzer_thread = threading.Thread(target=run_dl_simulator, args=(settings,publish_event,dl_callback,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("Led diode simulator started")
    else:
        print("Starting real led diode buzzer")
        buzzer_pin = settings['pin']
        buzzer_thread = threading.Thread(target=run_dl_loop, args=(buzzer_pin, 2, 2,stop_event))
        buzzer_thread.start()
        threads.append(buzzer_thread)
        print("Real led diode started")
