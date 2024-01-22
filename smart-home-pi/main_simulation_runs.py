import threading
import keyboard
from components.PI1.UDS.uds import run_dus
from components.PI1.PIR.pir import run_DS1, run_DPIR1, run_RPIR1, run_DPIR2, run_RPIR2, run_RPIR3, run_RPIR4
from components.PI1.DHT.dht import run_dht
from components.PI1.GYRO.gyro import run_gyro
from settings import load_settings
from components.PI1.MS.dms import run_dms
import time
from threading import Lock

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass

lock = Lock()

def automatic_sensors():

    #DS(button)
    ds1_settings = settings['DS1']
    run_DS1(ds1_settings, threads, stop_event, lock)

    ds2_settings = settings['DS2']
    run_DS1(ds2_settings, threads, stop_event, lock)



    #PIR (sensors)
    DPIR1_settings = settings['DPIR1']
    run_DPIR1(DPIR1_settings, threads, stop_event,lock)

    DPIR2_settings = settings['DPIR2']
    run_DPIR2(DPIR2_settings, threads, stop_event, lock)

    RPIR1_settings = settings['RPIR1']
    run_RPIR1(RPIR1_settings, threads, stop_event,lock)

    RPIR2_settings = settings['RPIR2']
    run_RPIR2(RPIR2_settings, threads, stop_event, lock)

    RPIR3_settings = settings['RPIR3']
    run_RPIR3(RPIR3_settings, threads, stop_event, lock)

    RPIR4_settings = settings['RPIR4']
    run_RPIR4(RPIR4_settings, threads, stop_event, lock)

    #GYROSCOPE
    gyro_settings = settings['GYRO']
    run_gyro(gyro_settings, threads, stop_event, lock)

    #DHT (temperature)
    dht1_settings = settings['DHT1']
    run_dht(dht1_settings, threads, stop_event,lock)

    dht2_settings = settings['DHT2']
    run_dht(dht2_settings, threads, stop_event, lock)

    dht3_settings = settings['DHT3']
    run_dht(dht3_settings, threads, stop_event, lock)

    dht4_settings = settings['DHT4']
    run_dht(dht4_settings, threads, stop_event, lock)

    gdht_settings = settings['GDHT']
    run_dht(gdht_settings, threads, stop_event, lock)


    #DMS (kaypads)
    dms_settings = settings['DMS']
    run_dms(dms_settings, threads, stop_event,lock)
    

    #DUS (distance)
    dus1_settings = settings['DUS1']
    run_dus(dus1_settings, threads, stop_event,lock)

    dus2_settings = settings['DUS2']
    run_dus(dus2_settings, threads, stop_event, lock)

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