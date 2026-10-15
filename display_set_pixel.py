from microbit import *


# 1. What does the following code do, explain what each number given to the set_pixel function must be responsible for.
display.set_pixel(0, 0, 9)
display.set_pixel(2, 2, 5)
THe following code operates essentially in the form of (movement right, movement down, brightness), and the pixel starts from the top left corner.

# 2. draw a pixel in the bottom right corner, full brightness
display.set_pixel(4, 4, 9)

# 3. Using the set_pixel function, how could you turn off all three LEDs (below the code where you turned them on)?
display.set_pixel(0 ,0 ,0)
display.set_pixel(2, 2, 0)
display.set_pixel(4, 4, 0)
Or you could change the brightness of the pixels in the original code. I essentially just made 0 brightness pixels overlap in the same positions as the original pixels.

# 4. Remove the code where you were able to turn off the individual LEDs. Verify that they stay on once more. Then, use the display.clear() function to turn off the whole display.
display.clear()
