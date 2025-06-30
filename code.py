# Write your code here :-)
#My name is Jacob Baker and this is Chapter 3 CPX Lab 1 and I am doing it on June 20. I am now revising on June 30
from adafruit_circuitplayground import cp
import time
while True:
    if cp.switch:
        cp.pixels[2] = (255, 0, 0)
    else:
        cp.pixels[2] = (0, 0, 0)
    if cp.button_a:
        cp.play_file("cash_register_x.wav")
    elif cp.button_b:
        cp.play_file("applause_y.wav")
    if cp.touch_A1:
        cp.pixels[1] = (0, 0, 255)
    else:
        cp.pixels[1] = (0, 0, 0)
