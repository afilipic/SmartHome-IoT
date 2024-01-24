import time
import random

def generate_values_sensors(settings):
    while True:
        state = random.randint(0, 1)
        if state < 0:
            state = False
        if state > 1:
            state = True
        yield state


def run_pir_simulator(settings,publish_event, callback, stop_event,lock,light_event=None,number_of_people_thread=None,home=None):
    delay = 2
    alarm = False
    while not stop_event.is_set():
        i = 0
        for s in generate_values_sensors(settings):
            if s == True and (settings["name"] == "Door PIR 2" or settings["name"] == "Door PIR 1"):
                number_of_people_thread.set()
            if s == True and (settings["name"] == "Room PIR 4" or settings["name"] == "Room PIR 3" or settings["name"] == "Room PIR 2"  or settings["name"] == "Room PIR 1"):
                if home and home.people_count == 0:
                    print("UKLJUCI ALARM")
                    home.set_alarm_true()
                    alarm = True
            time.sleep(delay)
            with lock:
                callback(s,publish_event,settings,light_event,number_of_people_thread,alarm)
            i += 1


