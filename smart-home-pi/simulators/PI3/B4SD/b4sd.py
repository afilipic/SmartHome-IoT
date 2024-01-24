import time

def generate_values():
    while True:
        current_time_with_colon = time.strftime("%H:%M")

        if (int(time.ctime()[18:19]) % 2 == 0):
            current_time_with_colon = time.strftime("%H %M")

        yield current_time_with_colon


def run_b4sd_simulator(settings, publish_event, b4sd_callback, stop_event):
    for message in generate_values():
        time.sleep(1)

        b4sd_callback(publish_event, settings, message)

        if stop_event.is_set():
            break
