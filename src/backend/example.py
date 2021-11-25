from overdrive import Overdrive
from  time import sleep
import threading

#rot 18-20-18
#blau 17-23-17

red_current_details = {'location': '', 'address' : '', 'piece': '', 'speed':'', 'clockwise': None}
blue_current_details = {'location': '', 'address' : '', 'piece': '', 'speed':'', 'clockwise': None}
test_rack = list()

red_speed = {'speed': 800, 'acc': 1000}
blue_speed = {'speed': 500, 'acc': 700}

map = []


def locationChangeCallback(addr, location, piece, speed, clockwise):
    # Print out addr, piece ID, location ID of the vehicle, this print everytime when location changed
    print("Location from " + str(addr) + " : " + "Piece=" + str(piece) +  " Speed=" + str(speed) + " Location=" + str(location) + " Clockwise=" + str(clockwise))
    global red_current_details
    global blue_current_details
    if 'ed:00:db:97:c2:de' in str(addr):
        red_current_details = {'location': str(location), 'address' : str(addr), 'piece': str(piece), 'speed': str(speed), 'clockwise': str(clockwise)}
    elif 'FD:97:48:FB:A7:FE' in str(addr):
        blue_current_details = {'location': str(location), 'address': str(addr), 'piece': str(piece), 'speed': str(speed),
                               'clockwise': str(clockwise)}

    else:
        print('Oops something went wrong inside locationChangeCallback')




def maneuver(car):
    car.changeLaneRight(500,500)

#def analyze(car):
#    # car blinking
#
#
 #   while True:
 #       # hier der Code, der mindestens einmal ausgeführt wird
 #       # ....
 #       if red_current_details['location'] != '':
 #           test_rack.append(red_current_details['location'])
 #           if test_rack.count(test_rack[0]) > 1 :
 #               print('break')
 #               car.changeSpeed(0,0)
 #               break

#    print(test_rack)


def checkCollision():
    global red_speed
    global blue_speed
    global red_current_details
    global blue_current_details

    blue_piece = blue_current_details['piece']
    red_piece = red_current_details['piece']

    if red_current_details['clockwise'] != blue_current_details['clockwise']:
        if (blue_piece == '17') and (red_piece == '18' or red_piece == '20' or red_piece=='23'):
           blue_speed['speed'] = 250
        else:
           blue_speed['speed'] = 500
   # else:
    #    print("sync")


def main():
    global red_speed
    global blue_speed
    mac_red = "ed:00:db:97:c2:de" #in echt red
    mac_blue = "FD:97:48:FB:A7:FE" #in echt blue
    red_car = Overdrive(mac_red)
    blue_car = Overdrive(mac_blue)
    cars = [blue_car,red_car]

    for car in cars:
        car.setLocationChangeCallback(locationChangeCallback)

  #  thread = threading.Thread(target=thread_function())
  #  thread.start()
    # initailer wert für 3 sekunden fahren, für die ersten callbacks

    red_car.changeLane(1000,1000,30)
    blue_car.changeLane(1000,1000,-30)

   # while True:
   #     sleep(0.2)
   #     piece = blue_current_details['piece']
   #     print(piece)
   #     if piece not in map:
   #         map.append(piece)



   # blue_car.changeSpeed(300,1000)
    #blue_car.changeLane(1000,1000,10)

    while True:
        checkCollision()
        red_car.changeSpeed(red_speed['speed'], red_speed['acc'])
        blue_car.changeSpeed(blue_speed['speed'], blue_speed['acc'])
        sleep(0.1)
   #     blue_car.changeSpeed(blue_speed['speed'], blue_speed['acc'])









    #input() # Hold the program so it won't end abruptly

if __name__ == "__main__":
    main()
