import RPi.GPIO as GPIO
import time
import threading

class DoorLight(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

def run_door_light_loop(light, delay, stop_event):
    while True:
        light.turn_on()
        time.sleep(delay)
        light.turn_off()
        if stop_event.is_set():
            break
        time.sleep(delay)
