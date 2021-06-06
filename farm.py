import mouse
import keyboard
from pynput import keyboard as pynput_keyboard
import time
import sys

# boolean for while loop that calls keyboard inputs
should_stop = False

# listener functions that detects key presses, ends program when 'End' is pressed
def on_press(key):
    global should_stop
    print(str(key))
    if key == pynput_keyboard.Key.end:
        print (str(key) + ' was pressed; ending')
        should_stop = True
        sys.exit()

# main loop for keyboard inputs using above function as listener
with pynput_keyboard.Listener(on_press=on_press) as listener:
    # tracks the last time that the shift key was pressed
    last_time_shift = time.time()
    # tracks the last time that mouse left click was clicked
    last_time_click = time.time()
    while not should_stop:
        # holds down shift every 0.1 seconds
        if (last_time_shift + 0.1 < time.time()):
            keyboard.press('shift')
            print('Shift pressed')
            last_time_shift += 0.1
        # left clicks every 0.25 seconds
        if (last_time_click + 0.25 < time.time()):
            mouse.click()
            print('Mouse left clicked')
            last_time_click += 0.25
    listener.join()
