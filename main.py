import sys
import threading
from threading import Lock


from components.DS1.ds1 import run_door_sensor
from components.DHT.dht import run_dht
from settings import load_settings
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
    print("| 1) DL                           |")
    print("| 2) DS1                          |")
    print("| 3) DUS                          |")
    print("| 4) DB                           |")
    print("| 5) DPIR1                        |")
    print("| 6) DMS                          |")
    print("| 7) RPIR1/RPIR2                  |")
    print("| 8) RDM1/RDM2                    |")
    print("| Enter x to exit                 |")
    print("|---------------------------------|")
    option = input("| Input number:").strip()
    print("|---------------------------------| \n")
    return option

def options(option):
    if option.lower() == 'x':
        sys.exit(0)

    if option == '2':
        ds1_settings = settings['DS1']
        run_door_sensor(ds1_settings, threads, stop_event)

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
