import sys
import threading

from components.PI1.BUZZ.db import run_door_buzzer
from components.BUTTONS.ds import run_door_sensor
from settings import load_settings

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
    print("| 2) DB                           |")
    print("| 3) DS                           |")
    print("| Enter x to exit                 |")
    print("|---------------------------------|")
    option = input("| Input number:").strip()
    print("|---------------------------------| \n")
    return option

def options(option):
    if option.lower() == 'x':
        sys.exit(0)


    #if option == '1':
    #    dl_settings = settings['DL']
    #    run_dl(dl_settings, threads, stop_event)


    elif option == '2':
        DB_settings = settings['DB']
        run_door_buzzer(DB_settings, threads, stop_event)

    elif option == '3':
        DS_settings = settings['DS1']
        run_door_sensor(DS_settings, threads, stop_event)


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
