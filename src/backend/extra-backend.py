from overdrive import Overdrive
import time
from time import sleep
import random
from random import randrange

#rot 18-20-18
#blau 17-23-17


class FancyBackend:
    def __init__(self, mac_addr):
        self._target_mac = mac_addr
        self._transitions = 0
        self._transition_time = time.perf_counter() # ??
        self._speed = 0
        self._battery = 0
        self._overdrive = Overdrive(mac_addr)

        # setup callbacks
        self.getOverdrive().setTransitionCallback(self.transitionCallback)
        self.getOverdrive().setBatteryCallback(self.batteryCallback)

    def getOverdrive(self):
        return self._overdrive

    def getTransitions(self):
        return self._transitions

    #TODO check
    def changeSpeed(self, new_speed, accel=1000):
        self.getOverdrive().changeSpeed(new_speed, accel)
        self._speed = speed

    def transitionCallback(self, addr):
        if addr == self._target_mac:
            self._transitions = (self._transitions + 1) % 8
        else:
            print(f"unexpected mac in transition callback [{addr}], expected [{self._target_mac}]")

    def batteryCallback(self, addr, batteryLevel):
        if addr == self._target_mac:
            self._battery = int((batteryLevel / 4200 )* 100)
        else:
            print(f"unexpected mac in battery callback [{addr}], expected [{self._target_mac}]")

#type slow, or fast brake
def carBrake(red_car, blue_car, diff_time, speed):

    if red_car.getTransitions() == 0 and diff_time > 0.6 and speed < 600:
        red_car.getOverdrive().setEngineLight(0, 15, 15)
        sleep(0.5)
        return red_car

    if diff_time > 0.3 and speed > 600:
        red_car.getOverdrive().setEngineLight(0, 0, 15)
        sleep(0.5)
        return red_car
    else:
        red_car.changeSpeed(0)
        red_car.getOverdrive().setEngineLight(15, 0, 0)

    return red_car

def random_speed():
    return random.choice([400, 700, 800])

def main():
    mac_red  = "ed:00:db:97:c2:de" #in echt red
    mac_blue = "FD:97:48:FB:A7:FE" #in echt blue

    red_car  = FancyBackend(mac_red)
    blue_car = FancyBackend(mac_blue)

    speed = 0

    red_car.getOverdrive().getBatteryLevel()
    red_car.getOverdrive().changeLane(1000, 1000, 50)
    red_car.changeSpeed(600) # red_speed
    blue_car.getOverdrive().changeLane(1000, 1000, -30)

    blue_car.changeSpeed(800) # blue_speed
    blue_car.getOverdrive().setEngineLight(15, 7, 10)

    sleep(1)

    ### Collision-Detection-ALgorithm
    while True:

        diff_time = time.perf_counter() - red_car.getTransitions()

        # NUMBER 1

        if (red_car.getTransitions() == 4) and (blue_car.getTransitions() == 7 or blue_car.getTransitions() == 0):
            print(f"Diff-time: {diff_time}")
            print("N1")
            stopped_car = carBrake(red_car, blue_car, diff_time, speed)
            while True:
                if blue_car.getTransitions() == 1 or blue_car.getTransitions() == 2:
                    sleep(0.5)
                    speed = random_speed()
                    stopped_car.changeSpeed(speed)
                    red_car.getOverdrive().setEngineLight(0, 15, 0)
                    break

        #N2
        if (red_car.getTransitions() == 0) and (blue_car.getTransitions() == 3 or blue_car.getTransitions() == 4):
            print(f"Diff-time: {diff_time}")

            print(f"N2 T_blue: {blue_car.getTransitions()} T_red={blue_car.getTransitions()}")
            stopped_car = carBrake(red_car, blue_car, diff_time, speed)

            while True:
                if blue_car.getTransitions() == 6:
                    speed = random_speed()
                    stopped_car.changeSpeed(speed)
                    red_car.setEngineLight(0, 15, 0)
                    break


