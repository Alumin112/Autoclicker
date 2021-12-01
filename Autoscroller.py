import keyboard
import mouse
while True:
    if keyboard.is_pressed('e'):
        mouse.wheel(10000000)
    if keyboard.is_pressed('w'):
        mouse.wheel(-10000000)
    if keyboard.is_pressed('q'):
        break