

from simulators.DHT.dht import run_dht_simulator
import threading
import time
callback_lock = threading.Lock()

def dht_callback(humidity, temperature, code):
    t = time.localtime()
    with callback_lock:
        print("\n--------DHT----------------------------------")
        print(f"Timestamp: {time.strftime('%H:%M:%S', t)}")
        print("-" * 45)
        print(f"Humidity: {humidity}%")
        print(f"Temperature: {temperature}°C")
        print("-" * 45 + "\n")


def run_dht(settings, threads, stop_event,lock):
        if settings['simulated']:
            print("DHT sensor simulation started")
            dht1_thread = threading.Thread(target = run_dht_simulator, args=(2, dht_callback, stop_event,lock))
            dht1_thread.start()
            threads.append(dht1_thread)
            print("RDHT1 sensor simulation started\n")
        else:
            from sensors.DHT.RDH1 import run_dht_loop, DHT
            print("Starting dht1 loop")
            dht = DHT(settings['pin'])
            dht1_thread = threading.Thread(target=run_dht_loop, args=(dht, 2, dht_callback, stop_event))
            dht1_thread.start()
            threads.append(dht1_thread)
            print("Dht1 loop started")
