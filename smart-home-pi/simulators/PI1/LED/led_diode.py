import time
import keyboard


def run_dl_simulator(settings, publish_event, dl_callback, stop_event,light_event):
    while not stop_event.is_set():
        light_event.wait()
        dl_callback(publish_event,settings,True)
        time.sleep(10)
        dl_callback(publish_event,settings,True)
        dl_callback(publish_event,settings,False)
        light_event.clear()