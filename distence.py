import time
import board
import adafruit_hcsr04

sonar=adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D12)
while True:
    try:
        print((sonar.distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)