
from backend.overdrive import Overdrive
import time
from time import sleep
import random
import threading

#rot 18-20-18
#blau 17-23-17


class FancyBackend:
    global carPositions
    carPositions = [0,0]

    def __init__(self, mac_addr):
        self._target_mac = mac_addr
        self._transitions = 0
        self._transition_time = time.perf_counter() # ??
        self._speed = 0
        self._battery = 0
        self._battery_callback = lambda i: None
        self._overdrive = Overdrive(mac_addr)
        # setup callbacks
        self.getOverdrive().setTransitionCallback(self.transitionCallback)
        self.getOverdrive().setBatteryCallback(self.batteryCallback)


    def getOverdrive(self):
        return self._overdrive

    def getTransitions(self):
        return self._transitions

    def getBatteryLevel(self):
        return self._battery

    def setBatteryLevelCallback(self, callback):
        self._battery_callback = callback

    def getTransitionTime(self):
        return self._transition_time

    #TODO check
    def changeSpeed(self, new_speed, accel=1000):
        self.getOverdrive().changeSpeed(new_speed, accel)
        self._speed = new_speed

    def transitionCallback(self, addr):
        global carPositions

        t = time.perf_counter()

        diff = self._transition_time - t
        self._transition_time = t
        self._transitions = (self._transitions + 1) % 8

        
        map_loc_file = open('/opt/lampp/htdocs/GTAIngolstadt/location.txt', 'w+')
        json_output = map_loc_file.readlines()
        map_loc_file.truncate(0)


        if addr.lower() in 'ed:00:db:97:c2:de':

            carPositions[0] = self._transitions
            new_json_str = '{\n \"red_car\": \"piece' + str(carPositions[0]) + '\",\n \"blue_car\": '
            new_json_str += '\"piece' + str(carPositions[1]) + '\"\n}'
            map_loc_file.write(new_json_str)
            json_output = map_loc_file.readlines()

            map_loc_file.close()

        elif addr.lower() in 'FD:97:48:FB:A7:FE'.lower():

            carPositions[1] = self._transitions
            new_json_str = '{\n \"red_car\": \"piece' + str(carPositions[0]) + '\",\n \"blue_car\": '
            new_json_str += '\"piece' + str(carPositions[1]) + '\"\n}'
            map_loc_file.write(new_json_str)
            json_output = map_loc_file.readlines()

            map_loc_file.close()
        else:
            print(f"unexpected mac in transition callback [{addr}], expected [{self._target_mac}]")

    def batteryCallback(self, addr, batteryLevel):
        if addr == self._target_mac:
            self._battery = int((batteryLevel / 4200 )* 100)
            self._battery_callback(self._battery)
        else:
            print(f"unexpected mac in battery callback [{addr}], expected [{self._target_mac}]")


class Tour:

    def __init__(self, get_red_car, get_blue_car):
        self.min_speed = 4
        self.max_speed = 7
        self.get_red_car  = get_red_car
        self.get_blue_car = get_blue_car

    def setMaxSpeed(self, new_speed):
        self.max_speed = new_speed

    def setMinSpeed(self, new_speed):
        self.min_speed = new_speed

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

    def random_speed(self):
        return random.randint(self.min_speed, self.max_speed) * 100

    def stop(self):
        self._stop = True

    def start(self):
        self._stop = False
        red_car = self.get_red_car()
        blue_car = self.get_blue_car()
        if red_car != None and blue_car != None:
            threading.Thread(target=self.mainloop, args=(red_car, blue_car)).start()
        else:
            print(f"not both cars are ready")

    def mainloop(self, red_car, blue_car):
        speed = 0
        red_car.getOverdrive().getBatteryLevel()
        red_car.getOverdrive().changeLane(1000, 1000, 50)
        red_car.changeSpeed(600) # red_speed
        blue_car.getOverdrive().changeLane(1000, 1000, -30)

        blue_car.changeSpeed(800) # blue_speed
        blue_car.getOverdrive().setEngineLight(15, 7, 10)

        sleep(1)

        ### Collision-Detection-ALgorithm
        while not self._stop:

            diff_time = time.perf_counter() - red_car.getTransitionTime();

            # NUMBER 1

            if (red_car.getTransitions() == 4) and (blue_car.getTransitions() == 7 or blue_car.getTransitions() == 0):
                print(f"Diff-time: {diff_time}")
                print("N1")
                stopped_car = Tour.carBrake(red_car, blue_car, diff_time, speed)
                while True:
                    if self._stop: break
                    if blue_car.getTransitions() == 2:
                        sleep(0.5)
                        speed = self.random_speed()
                        stopped_car.changeSpeed(speed)
                        red_car.getOverdrive().setEngineLight(0, 15, 0)
                        break

                if self._stop: break

                #N2
            if (red_car.getTransitions() == 0) and (blue_car.getTransitions() == 3 or blue_car.getTransitions() == 4):
                print(f"Diff-time: {diff_time}")

                print(f"N2 T_blue: {blue_car.getTransitions()} T_red={blue_car.getTransitions()}")
                stopped_car = Tour.carBrake(red_car, blue_car, diff_time, speed)

                while True:
                    if self._stop: break
                    if blue_car.getTransitions() == 6:
                        speed = self.random_speed()
                        stopped_car.changeSpeed(speed)
                        red_car.getOverdrive().setEngineLight(0, 15, 0)
                        break
                if self._stop: break


        red_car.changeSpeed(0)
        blue_car.changeSpeed(0)


if __name__ == "__main__":
    mac_red  = "ed:00:db:97:c2:de" #in echt red
    mac_blue = "FD:97:48:FB:A7:FE" #in echt blue

    red_car  = FancyBackend(mac_red)
    blue_car = FancyBackend(mac_blue)

    Tour(lambda: red_car, lambda: blue_car).start()
