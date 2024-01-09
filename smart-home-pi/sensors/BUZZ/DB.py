try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass
import time
import threading

class Buzzer(object):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

def run_buzzer_loop(buzzer, delay_on, delay_off, callback, stop_event):
    while not stop_event.is_set():
        buzzer.turn_on()
        time.sleep(delay_on)

        buzzer.turn_off()
        time.sleep(delay_off)

        callback()