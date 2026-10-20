# Imports go at the top
from microbit import *
import random

frame_count = 0
x = 2
y = 4
fall_x = random.randint(0,4)
fall_y = 0

while True:
    if fall_x == x and fall_y == y:
        display.show(Image.SAD)
        display.scroll("GAME OVER!", delay = 40 )
        break
        
    frame_count += 1
    if frame_count % 6 == 0:
        fall_y += 1
    if fall_y > 4:
        fall_y = 0
        fall_x = random.randint(0,4)

    if button_a.was_pressed() and x>0:
        x -= 1
    if button_b.was_pressed() and x<4:
        x += 1
        
    display.clear()
    display.set_pixel(x,y,9)
    display.set_pixel(fall_x,fall_y,9)

    sleep(50)
    
