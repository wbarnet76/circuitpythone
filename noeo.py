import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 1000

print("Make it red!")

while True:
    dot.fill((13, 22, 55))