import sys
import threading
from threading import Lock

import keyboard

from components.BUZZ.db import run_door_buzzer
from components.LED.led_diode import run_dl
from components.UDS.uds import run_DUS
from components.PIR.pir import run_DS1,run_DPIR1,run_RPIR1,run_RPIR2
from components.DHT.dht import run_dht
from settings import load_settings
from components.MS.dms import run_dms
import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass


def automatic_sensors():

    ds1_settings = settings['DS1']
    run_DS1(ds1_settings, threads, stop_event)

    dus_settings = settings['DUS']
    run_DUS(dus_settings, threads, stop_event)

    DPIR1_settings = settings['DPIR1']
    run_DPIR1(DPIR1_settings, threads, stop_event)

    DMS_settings = settings['DMS']
    run_dms(DMS_settings, threads, stop_event)

    RPIR1_settings = settings['RPIR1']
    run_RPIR1(RPIR1_settings, threads, stop_event)

    dht1_settings = settings['DHT1']
    run_dht(dht1_settings, threads, stop_event)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    print('----------Starting app--------------')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()

    def check_for_quit():
        while True:
            if keyboard.is_pressed('q'):  # Ako je pritisnut taster 'q'
                print("Quitting...")
                stop_event.set()  # Signalizira svim tredovima da se zaustave
                break
            time.sleep(0.1)  # Kratka pauza da se smanji opterećenje procesora

    quit_thread = threading.Thread(target=check_for_quit)
    quit_thread.start()  # Pokreće tred za proveru pritiska tastera 'q'

    try:
        while True:
            automatic_sensors()
            if stop_event.is_set():  # Proverava da li je događaj za zaustavljanje postavljen
                break
            stop_event.clear()
            threads = []
    except KeyboardInterrupt:
        print('---------------Stopping app----------------')
        stop_event.set()

    for t in threads + [quit_thread]:  # Čeka da se svi tredovi završe
        t.join()