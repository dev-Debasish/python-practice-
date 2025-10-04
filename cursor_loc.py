import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Cursor coordinates: X={x}, Y={y}", end="\r")  # Overwrites the same line
        time.sleep(0.1)  # Update every 100 ms
except KeyboardInterrupt:
    print("\nStopped.")
