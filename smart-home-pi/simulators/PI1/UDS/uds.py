import time
import random

def generate_values_door_sensor():
    distance = random.randint(0, 400)
    while True:
        distance = distance + random.randint(-50, 50)
        if distance < 0 or distance > 400:
            distance = random.randint(0, 400)
            yield 0

        yield distance


def run_dus_simulator(delay, dus_callback, stop_event, publish_event, settings, lock, number_of_people_thread,home):

    old_distance = 1000
    person_going_away = 0
    person_going_in = 0

    while not stop_event.is_set():
        number_of_people_thread.wait()
        i = 0
        for d in generate_values_door_sensor():
            if old_distance > d:
                person_going_away += 1
                person_going_in = 0
            if old_distance < d:
                person_going_in += 1
                person_going_away = 0

            if person_going_away > 2:
                with lock:  # Use the lock to safely modify the shared variable
                    home.less_people()
                print("osoba je otisla, trenutno ljudi u sobi:", home.people_count)

            if person_going_in > 2:
                with lock:
                    home.more_people()
                print("osoba je dosla, trenutno ljudi u sobi:", home.people_count)

            old_distance = d  # Update old_distance for the next iteration
            time.sleep(delay)
            dus_callback(stop_event, settings, publish_event, d,home.people_count)
            i += 1
            if i == 7:
                number_of_people_thread.clear()
                print("zavrsen posao")
