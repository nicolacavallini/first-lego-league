from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

mm = MotorPair("C","D")

cs_e = ColorSensor("E")

cs_f = ColorSensor("F")

mm.set_default_speed(5)

cs_guide = cs_e
cs_map = cs_f

cs_tmp = cs_e


while True:
    mm.start(50-cs_guide.get_reflected_light())
    #print(cs_f.get_reflected_light())

    if cs_map.get_reflected_light()<25:

        #for i in range(20):
        #    print("CAMBIO")

        #cs_tmp = cs_guide
        #cs_guide = cs_map
        #cs_map = cs_tmp

        mm.start_tank(-1,1)

        print("---->"+str(cs_guide.get_reflected_light()))

        #if cs_guide.get_reflected_light()<25:
        #    break
