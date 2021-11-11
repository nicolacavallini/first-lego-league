from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

motor_pair=MotorPair("E","F")
distance_sensor=DistanceSensor("A")

while True:
    distance=distance_sensor.get_distance_cm()
    print(distance)
    print(type(distance))
    if distance==None:
        distance=200

    if distance>20:
        motor_pair.set_default_speed(-20)
        motor_pair.start()
    elif distance<20:
        motor_pair.set_default_speed(20)
        motor_pair.start()
    else:
        motor_pair.stop()
