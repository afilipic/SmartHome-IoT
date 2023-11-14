import RPi.GPIO as GPIO
import time

class DoorSensor(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def is_open(self):
        return GPIO.input(self.pin)

def run_door_sensor_loop(sensor, callback, delay, stop_event):
    while True:
        door_status = sensor.is_open()
        callback(door_status)
        if stop_event.is_set():
            break
        time.sleep(delay)

