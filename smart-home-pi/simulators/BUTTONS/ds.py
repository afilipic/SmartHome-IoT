import keyboard
import time
import threading

key_pressed = False
start_time = None
alarm_on = False

def on_press(key):
    global key_pressed, start_time
    if key == keyboard.KeyCode.from_char('o'):
        if not key_pressed:
            key_pressed = True
            start_time = time.time()
            print("Vrednost: 1")

def on_release(key):
    global key_pressed, start_time, alarm_on
    if key == keyboard.KeyCode.from_char('o'):
        key_pressed = False
        elapsed_time = time.time() - start_time
        print("Vrednost: 0")
        if elapsed_time > 5 and alarm_on:
            print("Alarm je ugašen")
            alarm_on = False

def check_alarm(stop_event):
    global key_pressed, start_time, alarm_on
    while not stop_event.is_set():
        if key_pressed and not alarm_on:
            if time.time() - start_time > 5:
                print("Alarm je upaljen")
                alarm_on = True
        time.sleep(0.1)

def run_key_monitor(stop_event):
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    check_alarm(stop_event)
    listener.join()