from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def block_wise_arm_motion():
    for i in range(10):
        lifting_arm.run_for_seconds(.1,-2)
        print("i = "+str(i)+", angle = "+str(lifting_arm.get_position()),", distance= "+str(distance_sensor.get_distance_cm()))


def move_grab_move():
    lifting_arm.run_for_seconds(1.,-20)

    #movement_motors.move(20,'cm',0)
    movement_motors.start()
    distance_sensor.wait_for_distance_closer_than(16,'cm')
    movement_motors.stop()

    lifting_arm.run_for_seconds(1.,20)
    movement_motors.move(7,'cm',0)
    lifting_arm.run_for_seconds(1.,-20)
    movement_motors.move(-7,'cm',0)

def move_arm():
    lifting_arm.run_to_position(0,"shortest path",20)

    for i in range(20):
        lifting_arm.run_for_degrees(1,2)
        print("i = "+str(i)+", angle = "+str(lifting_arm.get_position()),", distance= "+str(distance_sensor.get_distance_cm()),", degrees conted = "+str(lifting_arm.get_degrees_counted()))







driving_base = PrimeHub()

movement_motors = MotorPair('C','D')
distance_sensor = DistanceSensor('F')
lifting_arm = Motor('E')


driving_base.light_matrix.show_image('HAPPY')

movement_motors.set_default_speed(20)

#movement_motors.move_tank(20,"cm",50,30)
