
import threading
from settings import load_settings
from components.DHT.dht import run_dht
from components.MS.dms import run_dms
from components.UDS.uds import run_dus

import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass

def run_simulators(stop_event):

    dht1_settings = settings['DHT1']
    run_dht(dht1_settings, threads, stop_event)

    dms_settings = settings['DMS']
    run_dms(dms_settings, threads, stop_event)

    dus_settings = settings['DUS']
    run_dus(dus_settings, threads, stop_event)



if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    try:
        run_simulators(stop_event)
        # stop_event.clear()
        # threads = []
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
