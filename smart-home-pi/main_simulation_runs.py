import threading
import keyboard
from components.PI1.UDS.uds import run_dus
from components.PI1.PIR.pir import run_DPIR1, run_RPIR1, run_DPIR2, run_RPIR2, run_RPIR3, run_RPIR4
from components.PI1.DHT.dht import run_dht
from components.PI1.GYRO.gyro import run_gyro
from settings import load_settings
from components.PI1.MS.dms import run_dms
from components.PI1.LCD.lcd import run_lcd
from components.PI1.LED.led_diode import run_dl
import paho.mqtt.client as mqtt
import time
from threading import Lock
import json
from queue import Queue
from home import Home

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass

lock = Lock()

number_of_people = 0
alarm = False

number_of_people_thread = threading.Event()

alarm_event = threading.Event()

light_event = threading.Event()
print_lock = threading.Lock()
gdht_queue = Queue()
mqtt_client = mqtt.Client()
home = Home("1111")
# Ovo je sada obična funkcija, a ne lambda, kako bi mogli da prosledimo 'home' objekat
def on_message(client, userdata, msg):

    global home
    data = json.loads(msg.payload.decode('utf-8'))
    topic = msg.topic  # Dobijate topik poruke
    # Ovde ide logika za obradu poruka...
    if topic == "activate_alarm":
        print()
        # Obradi temperaturu
    elif topic == "deactivate_alarm":
        print()
        # Obradi senzor
    elif topic == "schedule_alarm":
        # Postavi alarm status
        data = json.loads(msg.payload.decode('utf-8'))
        #home.set_alarm(data["value"])

def mqtt_client_thread():
    mqtt_client.connect("localhost", 1883, 60)
    mqtt_client.subscribe("activate_alarm")
    mqtt_client.subscribe("deactivate_alarm")
    mqtt_client.subscribe("schedule_alarm")
    print("mqtt thread je dodat")
    mqtt_client.loop_forever()

def automatic_sensors():
    global home

    mqtt_thread = threading.Thread(target=mqtt_client_thread)
    mqtt_thread.start()
    threads.append(mqtt_thread)

    #LED
    dl_settings = settings['DL']
    run_dl(dl_settings, threads, stop_event,light_event)

    # LCD
    glcd_settings = settings["GLCD"]
    run_lcd(glcd_settings, threads, stop_event, print_lock, gdht_queue)

    #PIR (sensors)
    DPIR1_settings = settings['DPIR1']
    run_DPIR1(DPIR1_settings, threads, stop_event,lock,light_event,number_of_people_thread)

    DPIR2_settings = settings['DPIR2']
    run_DPIR2(DPIR2_settings, threads, stop_event, lock,light_event,number_of_people_thread)

    RPIR1_settings = settings['RPIR1']
    run_RPIR1(RPIR1_settings, threads, stop_event,lock,home)

    RPIR2_settings = settings['RPIR2']
    run_RPIR2(RPIR2_settings, threads, stop_event, lock,home)

    RPIR3_settings = settings['RPIR3']
    run_RPIR3(RPIR3_settings, threads, stop_event, lock,home)

    RPIR4_settings = settings['RPIR4']
    run_RPIR4(RPIR4_settings, threads, stop_event, lock,home)

    #GYROSCOPE
    gyro_settings = settings['GYRO']
    run_gyro(gyro_settings, threads, stop_event, lock,alarm_event)

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
    run_dht(gdht_settings, threads, stop_event, lock,gdht_queue)


    #DMS (kaypads)
    dms_settings = settings['DMS']
    run_dms(dms_settings, threads, stop_event,lock)
    

    #DUS (distance)
    dus1_settings = settings['DUS1']
    run_dus(dus1_settings, threads, stop_event,lock,number_of_people_thread,home)

    dus2_settings = settings['DUS2']
    run_dus(dus2_settings, threads, stop_event, lock,number_of_people_thread,home)

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