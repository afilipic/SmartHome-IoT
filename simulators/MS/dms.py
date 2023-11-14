import time
import random

def run_dms_simulator(delay, stop_event):
    valid_values = {"1", "2", "3", "A", "4", "5", "6", "B", "7", "8", "9", "C", "*", "0", "#", "D"}
    sensored_values = []
    while True:
        generated_value = random.choice(list(valid_values))
        print(f"Keypad button {generated_value} value sensored")
        sensored_values.append(generated_value)
        time.sleep(delay)
        if stop_event.is_set():
            break
        '''elif key_press == 'Q':
            print("Exiting keypad simulation.")
            break
        else:
            print("Invalid button. Please press a valid button.")
            
    if sensored_values:
        print("Buttons sensored during the simulation:")
        print(", ".join(sensored_values))
    else:
        print("No buttons were pressed during the simulation.")'''