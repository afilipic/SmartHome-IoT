

from simulators.DHT.dht import run_dht_simulator
import threading
import time

def dht_callback(humidity, temperature, code):
    t = time.localtime()
    print("-"*20)
    print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
    print("-" * 20)
    print(f"Humidity: {humidity}%")
    print(f"Temperature: {temperature}°C\n")


def run_dht(settings, threads, stop_event):
        if settings['simulated']:
            print("Starting RDM1 sumilator")
            dht1_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event))
            dht1_thread.start()
            threads.append(dht1_thread)
            print("RDM1 sumilator started\n")
        else:
            from sensors.DHT.RDH1 import run_dht_loop, DHT
            print("Starting dht1 loop")
            dht = DHT(settings['pin'])
            dht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event))
            dht1_thread.start()
            threads.append(dht1_thread)
            print("Dht1 loop started")
