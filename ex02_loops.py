from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

from time import sleep

def show_for_loop():

    lifting_arm.run_to_position(0,"shortest path",20)

    amplitude = 20
    speed = 10

    for i in range(0,20,1):
        print(1)
        lifting_arm.run_for_degrees(amplitude,speed)
        lifting_arm.run_for_degrees(-amplitude,speed)



def while_loop_test_00():

    distance = 201

    movement_motors.set_default_speed(20)

    #movement_motors.start()
    #distance_sensor.wait_for_distance_closer_than(15,'cm')
    #movement_motors.stop()

    movement_motors.start()
    while distance >15:

        distance = distance_sensor.get_distance_cm()
        print(distance)
        sleep(.1)

    movement_motors.stop()

def while_loop_test_01():

    while True:
        driving_base.left_button.wait_until_pressed()

        distance = 201

        movement_motors.set_default_speed(20)

        movement_motors.start()
        while distance >15:

            distance = distance_sensor.get_distance_cm()
            print(distance)
            sleep(.1)

        movement_motors.stop()

        # -->>> exercise: make it crash!





driving_base = PrimeHub()

driving_base.light_matrix.show_image('HAPPY')

movement_motors = MotorPair('C','D')
distance_sensor = DistanceSensor('F')
lifting_arm = Motor('E')

while_loop_test_01()
