import time
import random

def simulated_dms():
    valid_values = {"1", "2", "3", "A", "4", "5", "6", "B", "7", "8", "9", "C", "*", "0", "#", "D"}
    sensored_values = []
    print("Type 'q' to exit or press 'n' to get next value:")
    while True:
        key_press = input(">> ").upper()
        if key_press == 'N':
            generated_value = random.choice(list(valid_values))
            print(f"Keypad button {generated_value} value sensored")
            sensored_values.append(generated_value)
        elif key_press == 'Q':
            print("Exiting keypad simulation.")
            break
        else:
            print("Invalid button. Please press a valid button.")
        time.sleep(0.2)  # Debounce delay

    if sensored_values:
        print("Buttons sensored during the simulation:")
        print(", ".join(sensored_values))
    else:
        print("No buttons were pressed during the simulation.")