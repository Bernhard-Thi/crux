from overdrive import Overdrive
import time
from time import sleep
import random
from random import randrange

#rot 18-20-18
#blau 17-23-17

transitions_red = 0
transitions_blue = 0

transition_time_red = 0

red_speed = 600
blue_speed = 800

blue_battery = 0
red_battery = 0

# Setter für Felix
def setRedSpeed(val):
    global red_speed
    red_speed = val

def setBlueSpeed(val):
    global blue_speed
    blue_speed = val




def transitionCallback(addr):
    global transitions_red
    global transitions_blue
    global transition_time_red

    transition_time_red = time.perf_counter()

    #red car
    if addr == 'ed:00:db:97:c2:de':
        transitions_red += 1
        if transitions_red == 8:
            transitions_red = 0
        #print("Transition Update: " + addr +  " Count: " +  str(transitions_red))
    else:
        transitions_blue +=1
        if transitions_blue == 8:
            transitions_blue = 0
        #print("Transition Update: " + addr +  " Count: " +  str(transitions_blue))

def batteryCallback(addr, batteryLevel):
    global blue_battery
    global red_battery

    batteryLevelConverted = int((batteryLevel / 4200 )* 100)


    if addr == "FD:97:48:FB:A7:FE":
        blue_battery = batteryLevelConverted
    #    print(str(batteryLevel) + "Blue car " + "Battery Level: " + str(batteryLevelConverted) + '%')

    else:
        red_battery = batteryLevelConverted
        #print(str(batteryLevel) + "Red car " + "Battery Level: " + str(batteryLevelConverted) + '%')

#type slow, or fast brake
def carBrake(red_car, blue_car, diff_time, speed):
    global transitions_red

    if transitions_red == 0 and diff_time >0.6 and speed <600:
        red_car.setEngineLight(0,15,15)
        sleep(0.5)
        return red_car

    if (diff_time>0.3 and speed >600 ):
        red_car.setEngineLight(0,0,15)
        sleep(0.5)
        return red_car
    else:
        red_car.changeSpeed(0,1000)
        red_car.setEngineLight(15,0,0)


    return red_car


def main():
    global transition_time_red

    speed_list = [400,700,800]
    mac_police = "d0:6b:5a:6b:3a:10"
    mac_red = "ed:00:db:97:c2:de" #in echt red
    mac_blue = "FD:97:48:FB:A7:FE" #in echt blue
    red_car = Overdrive(mac_red)
    blue_car = Overdrive(mac_blue)
    #police_car = Overdrive(mac_police)
    #police_car.setLights(0x4C)
    cars = [blue_car,red_car]

    speed_random = 0

    for car in cars:
        car.setTransitionCallback(transitionCallback)
        car.setBatteryCallback(batteryCallback)


    red_car.getBatteryLevel()
    red_car.changeLane(1000,1000,50)
    red_car.changeSpeed (red_speed,1000)
    blue_car.changeLane(1000,1000,-30)

    blue_car.changeSpeed(blue_speed,1000)
    blue_car.setEngineLight(15,7,10)
    sleep(1)

    ### Collision-Detection-ALgorithm
    while True:

        diff_time = time.perf_counter() - transition_time_red


        # NUMBER 1

        if (transitions_red == 4) and (transitions_blue == 7 or transitions_blue == 0):
            print("Diff-time: " + str(diff_time))
            print("N1")
            stopped_car = carBrake(red_car, blue_car, diff_time, speed_random)
            while True:
                if transitions_blue == 1 or  transitions_blue == 2:
                    sleep(0.5)
                    speed_random = random.choice(speed_list)
                    stopped_car.changeSpeed(speed_random,1000)
                    red_car.setEngineLight(0,15,0)
                    break

        #N2

        if (transitions_red == 0) and (transitions_blue == 3 or transitions_blue == 4):
            print("Diff-time: " + str(diff_time))

            print("N2" + "T_blue: " + str(transitions_blue) + " T_red=" + str(transitions_red))
            stopped_car = carBrake(red_car, blue_car, diff_time, speed_random)

            while True:
                if transitions_blue == 6:
                    speed_random = random.choice(speed_list)
                    stopped_car.changeSpeed(speed_random,1000)
                    red_car.setEngineLight(0,15,0)
                    break




if __name__ == "__main__":
    main()
