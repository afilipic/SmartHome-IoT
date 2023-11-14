import time

try:
    import RPi.GPIO as GPIO
except:
    pass


def motion_detected():
    print("RPIR1 sensor is detecting something!")


def motion_not_detected():
    print("RPIR1 sensor is detecting nothing")


def run_rpir1_loop(PIR_PIN):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN)

        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=lambda x: motion_detected())

        print("Pritisni Ctrl+C za izalz")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nPrekinut senzor RPIR1")
    finally:
        GPIO.cleanup()