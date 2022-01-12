
import tkinter as tk
import tkinter.ttk as ttk
from backend.simple import Tour, FancyBackend


from tkinter import Tk, BOTH, END, LEFT, RAISED, RIDGE, RIGHT, Y, Scale, HORIZONTAL, Button, OptionMenu, \
    StringVar
from tkinter.ttk import Frame, Label, Entry

class ParaFrame(Frame):
    def __init__(self, container, tour):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self._tour = tour
        self.__create_widgets()

    def __create_widgets(self):
        start_button = ttk.Button(self, text="Start")
        start_button.bind('<Button-1>', self.start_tour)
        start_button.grid(column=0, row=0)

        stop_button = ttk.Button(self, text="Stop")
        stop_button.bind('<Button-1>', self.stop_tour)
        stop_button.grid(column=1, row=0)

        min_speed_frame = ScaleFrame(self, "min speed", self.set_min_speed, self._tour.min_speed)
        min_speed_frame.grid(column=0, row=1)

        max_speed_frame = ScaleFrame(self, "max speed", self.set_max_speed, self._tour.max_speed)
        max_speed_frame.grid(column=1, row=1)

    def set_max_speed(self, new_speed):
        self.tour.setMaxSpeed(new_speed)

    def set_min_speed(self, new_speed):
        self.tour.setMinSpeed(new_speed)

    def start_tour(self, event):
        self.tour.start()

    def stop_tour(self, event):
        self.tour.stop()


class ScaleFrame(Frame):
    def __init__(self, container, desc, callback, init):
        super().__init__(container)
        self.i_callback = callback

        label_max_speed = Label(self, text=desc, width=48, anchor="se")
        label_max_speed.grid(column=0, row=0)

        scale_single_car_speed = Scale(
            self,
            from_=100,
            to=800,
            orient=HORIZONTAL,
            length=200,
            command=self.handle_scale
        )
        scale_single_car_speed.grid(column=1, row=0)

    def handle_scale(self, i):
        self.i_callback(i)



# ###### ------- Connection Bereich: ------- #######
class CarFrame(ttk.Frame):
    def __init__(self, container, name, default_mac):
        super().__init__(container)

        self.car_name = name
        self.backend = None

        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.__create_widgets(default_mac)

    def __create_widgets(self, default_mac):
# --- Verbindungen ---
        label_single_car_connection = ttk.Label(
            self,
            text=f"Verbundenes Einzelauto [{self.car_name}] - MAC Adresse",
            width=48,
            anchor="w"
        )
        label_single_car_connection.pack()

# --- MAC-Adressen der Fahrzeuge ---

        button_connect = Button(self, text="Verbinden")
        button_connect.bind('<Button-1>', self.connect)
        button_connect.pack()

        self.mac_entry = Entry(self)
        self.mac_entry.pack()
        self.mac_entry.insert(END, default_mac)

        self.label_battery = Label(self, text="Batterieanzeige: ", width=48)
        self.label_battery.pack()

    def updateBatteryLevel(self, level):
        self.label_battery.config(text = f"Batterieanzeige: {level}%")

    def getMac(self):
        return self.mac_entry.get()

    def getBackend(self):
        return self.backend;

    def connect(self, event):
        mac = self.getMac()
        print(f"conecting to {mac}")
        be = FancyBackend(mac)
        if be._connected:
            self.backend = be
        else:
            print(f"{self.car_name} failed to connect to {mac} ")


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Replace')
        self.geometry('400x150')
        # windows only (remove the minimize/maximize button)

        # layout on the root window
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.tour = Tour(self.getRedCar, self.getBlueCar)

        self.__create_widgets()

    def getRedCar(self):
        return self.red_car_frame.getBackend()

    def getBlueCar(self):
        return self.blue_car_frame.getBackend()

    def __create_widgets(self):
        #default values
        mac_list = [ "ed:00:db:97:c2:de", "fd:97:48:fb:a7:fe" ]
        # create the button frame
        self.red_car_frame  = CarFrame(self, "rot", mac_list[0])
        self.red_car_frame.grid(column=0, row=0)

        # create the button frame
        self.blue_car_frame = CarFrame(self, "blau", mac_list[1])
        self.blue_car_frame.grid(column=1, row=0)

        # create the input frame
        input_frame = ParaFrame(self, self.tour)
        input_frame.grid(column=0, row=1, columnspan=3)



def main():
    app = App()
    app.mainloop()
