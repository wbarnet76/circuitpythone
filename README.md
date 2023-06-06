## Bowling_Ball_Arm 

### Description & Code
The purpose of this assignment was to create a specialized robot arm. The arm we created was a gravity-run mini bowling ball arm. The box was on a turn table, and then the arm itself was on an ball bearing axel. There was a servo with an arm above it that would spin and lock in the arm and then keep spinning to raise it. Then when it reached a certain angle the crank arm would slide out. After it would slide out then the arm would be free to swing down on the axel. Then a button would be pressed and the clamps would release the ball and it would fly forward hitting the targets. In total there would be 4 buttons and a potentiometer. The buttons would control the servo to lift up the arm and the release of the claw. The potentiometer would control the heading of the turntable. 
```python
import time
import board
import pwmio
import simpleio 
from adafruit_motor import servo
from analogio import AnalogIn 
from digitalio import DigitalInOut, Direction, Pull

button_a = DigitalInOut(board.D1)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.D2)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

button_c = DigitalInOut(board.D3)
button_c.direction = Direction.INPUT
button_c.pull = Pull.DOWN

button_d = DigitalInOut(board.D4)
button_d.direction = Direction.INPUT
button_d.pull = Pull.DOWN

pot = AnalogIn(board.A1)   

# create a PWMOut object on Pin A2.
pwm_servo = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
pwm_servo1 = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
pwm_servo2 = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)


# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm_servo, min_pulse=1000, max_pulse=2000)  # tune pulse for specific servo
my_servo1 = servo.Servo(pwm_servo1)
my_servo2 = servo.Servo(pwm_servo2)

while True:
    if button_a.value:
        my_servo.throttle  = 1
        print("servo counterclockwise")
        time.sleep(0.1)
    elif button_b.value:
        my_servo.throttle = -.05
        print("servo clockwise")
        time.sleep(0.1)

    elif button_c.value:
        my_servo1.angle = 0
        print("servo 1 counterclockwise")
        time.sleep(0.1)
    elif button_d.value:
        my_servo1.angle = 180
        print("servo 1 clockwise")
        time.sleep(0.1)

    else:
        print((int(simpleio.map_range(pot.value,0,65535,0,180)) ))
        newpot = int(simpleio.map_range(pot.value,0,65535,0,180))
        my_servo2.angle = newpot

        my_servo.throttle = 0
        print("servo off")
        time.sleep(0.1)
```
### Prototype:

![prototype_pic](/docs/IMG-5075.jpg)


### Circuit with all the servos running:

#### Crank/release servo:

![big_servo_1](/docs/ezgif.com-video-to-gif%20(5).gif)
#### Turntable servo:
![big_servo_2](/docs/ezgif.com-video-to-gif%20(6).gif)
#### Gripper servo:
![small_servo](/docs/ezgif.com-video-to-gif%20(7).gif)


### Assembled CAD (as is):

![CAD](/docs/cadarm.png)
### Wiring
![robotarm](https://github.com/vjones2906/circuitPython/blob/master/docs/robotarm_wiring.png)
### Reflection
This project was a challenge for my group. We didn't end up finishing everything and didn't even laser cut the CAD model. The plan was to split the CAD and code between the group members so that Vinnie did all the code and did the circuit while Will did all the CAD. Vinnie ended up finishing the code early and jonied will in trying to finish the CAD. Beacause of how the dimensions were done in CAD before Vinnie came, he had to define and redo most of the dimensions. This slowed down the proccess significantly. The group spent time making CAD parts before thinking them through to completion, which only made more work for them later. Will also missed quite a few days during the in-class time to work on the project, and not all the classtime we had was spent in a productive matter. If the group had spent any amount of time on the project after school or if they used the time they had wisely, the project could have been completed. In the end the group had a perfectly functioning circuit and code, a CAD document that was close to completion, and a prototype. All the group had to do to complete their project was finish, cut, and assemble the CAD shell. 



## PID_car


## ![IMG_1185](https://github.com/wbarnet76/circuitpythone/assets/71402909/9e8a8969-b370-4e9b-b771-b451c1e321c5)

https://github.com/wbarnet76/circuitpythone/assets/71402909/dfb7f9e0-965e-458a-bc1d-e2979a15df4f

###Reflection

for this project i saw Mr derolf's car thet he had made and it looked like a fun chalenge i was not ready for the chalenge tho. most of this project was above my coding abulty not because of the class but becuse of my own skill or lack there of. i reused a car that i had made for last years drag race and made modafacations on it to make it fit my new projects needs. the car had some flaws that i had not forseen like the axle and the thing tat he;d the axle was not built to leave room for movment or the ultrasonic plate was eyeballed and not made to the acual mesurments of the real life senser. the down fall of this project was the fact that me and matt may make a good freands but we get no work done because of that and so we spent most of the time aguing about the best fruit or best fast food frys and not acualy woking. 



