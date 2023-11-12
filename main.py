import sys
import threading
from threading import Lock

from components.BUZZ.DB import run_door_buzzer
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


def menu():
    print("|---------------------------------|")
    print("|  Choose sensor for simulation:  |")
    print("|---------------------------------|")
    print("| 1) DS1                          |")
    print("| 2) DL                           |")
    print("| 3) DUS                          |")
    print("| 4) DB                           |")
    print("| 5) DPIR1                        |")
    print("| 6) DMS                          |")
    print("| 7) RPIR1/RPIR2                  |")
    print("| 8) RDH1/RDHT2                   |")
    print("| Enter x to exit                 |")
    print("|---------------------------------|")
    option = input("| Input number:").strip()
    print("|---------------------------------| \n")
    return option

def options(option):
    if option.lower() == 'x':
        sys.exit(0)

    if option == '1':
        ds1_settings = settings['DS1']
        run_DS1(ds1_settings, threads, stop_event)

    elif option == '2':
        dl_settings = settings['DL']
        run_dl(dl_settings, threads, stop_event)

    elif option == '3':
        dus_settings = settings['DUS']
        run_DUS(dus_settings, threads, stop_event)


    elif option == '4':
        DB_settings = settings['DB']
        run_door_buzzer(DB_settings, threads, stop_event,print_lock=0)

    elif option == '5':
        DPIR1_settings = settings['DPIR1']
        run_DPIR1(DPIR1_settings, threads, stop_event)

    elif option == '6':
        DMS_settings = settings['DMS']
        run_dms(DMS_settings, threads, stop_event)

    elif option == '7':
        RPIR1_settings = settings['RPIR1']
        run_RPIR1(RPIR1_settings, threads, stop_event)

    elif option == '8':
        dht1_settings = settings['DHT1']
        run_dht(dht1_settings, threads, stop_event)

    else:
        print("Invalid input")

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    try:
        while True:
            option = menu()
            options(option)
            stop_event.clear()
            threads = []
    except KeyboardInterrupt:
        print('Stopping app')
        for t in threads:
            stop_event.set()
