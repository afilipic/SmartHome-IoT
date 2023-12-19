import threading
import keyboard
from components.UDS.uds import run_dus
from components.PIR.pir import run_DS1,run_DPIR1,run_RPIR1
from components.DHT.dht import run_dht
from settings import load_settings
from components.MS.dms import run_dms
import time
from threading import Lock

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass

lock = Lock()

def automatic_sensors():

    #Sensors
    ds1_settings = settings['DS1']
    run_DS1(ds1_settings, threads, stop_event,lock)

    DPIR1_settings = settings['DPIR1']
    run_DPIR1(DPIR1_settings, threads, stop_event,lock)

    RPIR1_settings = settings['RPIR1']
    run_RPIR1(RPIR1_settings, threads, stop_event,lock)

    #Temperature/Humidity
    dht1_settings = settings['DHT1']
    run_dht(dht1_settings, threads, stop_event,lock)

    #Kaypads
    dms_settings = settings['DMS']
    run_dms(dms_settings, threads, stop_event,lock)

    #Distance
    dus_settings = settings['DUS']
    run_dus(dus_settings, threads, stop_event,lock)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    print('----------Starting app--------------')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()

    try:
        while True:
            automatic_sensors()
            if stop_event.is_set():
                break
            stop_event.clear()
            threads = []
    except KeyboardInterrupt:
        print('---------------Stopping app----------------')
        stop_event.set()
        for t in threads:
            t.join()