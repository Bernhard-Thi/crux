from overdrive import Overdrive
import time
from time import sleep
import random
from random import randrange

#rot 18-20-18
#blau 17-23-17

#red_speed = 600
#blue_speed = 800

class FancyBackend:
    def __init__(self, mac_addr):
        self._target_mac = mac_addr
        self._transitions = 0
        self._transition_time = time.perf_counter() # ??
        self._speed = 0
        self._battery = 0
        self._overdrive = Overdrive(mac_addr)

    def getOverdrive(self):
        return self._overdrive

    def getTransitions(self):
        return self._transitions

    #TODO check
    def setSpeed(self, speed):
        self._speed = speed

    def transitionCallback(self, addr):
        if addr == self._target_mac:
            self._transitions = (self._transitions + 1) % 8
        else:
            print(f"unexpected mac in transition callback: [#{self._target_mac}]")

    def batteryCallback(self, addr, batteryLevel):
        if addr == self._target_mac:
            self._battery = int((batteryLevel / 4200 )* 100)
        else:
            print(f"unexpected mac in battery callback: [#{self._target_mac}]")

#type slow, or fast brake
def carBrake(red_car, blue_car, diff_time, speed):
    global transitions_red

    if red_car.getTransitions() == 0 and diff_time > 0.6 and speed < 600:
        red_car.getOverdrive().setEngineLight(0, 15, 15)
        sleep(0.5)
        return red_car

    if diff_time > 0.3 and speed > 600:
        red_car.getOverdrive().setEngineLight(0, 0, 15)
        sleep(0.5)
        return red_car
    else:
        red_car.getOverdrive().changeSpeed(0, 1000)
        red_car.getOverdrive().setEngineLight(15, 0, 0)

    return red_car

def random_speed():
    return random.choice([400, 700, 800])

def main():
    global transition_time_red

    mac_red  = "ed:00:db:97:c2:de" #in echt red
    mac_blue = "FD:97:48:FB:A7:FE" #in echt blue

    red_car  = FancyBackend(mac_red)
    blue_car = FancyBackend(mac_blue)

    speed = 0

    for car in [blue_car, red_car]:
        car.getOverdrive().setTransitionCallback(transitionCallback)
        car.getOverdrive().setBatteryCallback(batteryCallback)


    red_car.getOverdrive().getBatteryLevel()
    red_car.getOverdrive().changeLane(1000, 1000, 50)
    red_car.getOverdrive().changeSpeed(red_speed, 1000)
    blue_car.getOverdrive().changeLane(1000, 1000, -30)

    blue_car.getOverdrive().changeSpeed(blue_speed, 1000)
    blue_car.getOverdrive().setEngineLight(15, 7, 10)

    sleep(1)

    ### Collision-Detection-ALgorithm
    while True:

        diff_time = time.perf_counter() - transition_time_red

        # NUMBER 1

        if (transitions_red == 4) and (transitions_blue == 7 or transitions_blue == 0):
            print("Diff-time: " + str(diff_time))
            print("N1")
            stopped_car = carBrake(red_car, blue_car, diff_time, speed)
            while True:
                if transitions_blue == 1 or transitions_blue == 2:
                    sleep(0.5)
                    speed = random_speed()
                    stopped_car.changeSpeed(speed, 1000)
                    red_car.setEngineLight(0, 15, 0)
                    break

        #N2

        if (transitions_red == 0) and (transitions_blue == 3 or transitions_blue == 4):
            print("Diff-time: " + str(diff_time))

            print("N2" + "T_blue: " + str(transitions_blue) + " T_red=" + str(transitions_red))
            stopped_car = carBrake(red_car, blue_car, diff_time, speed_random)

            while True:
                if transitions_blue == 6:
                    speed_random = random_speed()
                    stopped_car.changeSpeed(speed_random,1000)
                    red_car.setEngineLight(0,15,0)
                    break


