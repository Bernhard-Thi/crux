from tkinter import Tk, BOTH, LEFT, RAISED, RIDGE, RIGHT, Y, Scale, HORIZONTAL, Button, OptionMenu, \
    StringVar
from tkinter.ttk import Frame, Label, Entry

from backend.simple import Tour, FancyBackend


def main():
    root = Tk()
    root.geometry("800x525")
    app = Gui()
    root.mainloop()


class Gui(Frame):
#    def __init__(self, _backend):
    def __init__(self):
        super().__init__()
        self.tour = Tour(lambda: self.car_first, lambda: self.car_second )
        self.init_ui()

    def init_ui(self):

        self.master.title("crux")
        self.pack(fill=BOTH, expand=True)

# ###### ------- Linke Seite: ------- #######
        left_side = Frame(self, relief=RAISED, borderwidth=2)
        left_side.pack(side=LEFT, fill=Y)

        label_single_car = Label(
            left_side,
            text="Einzelfahrzeug",
            width=50,
            anchor="center",
            background="red",
            relief=RAISED
        )
        label_single_car.pack()

# ###### ------- Connection Bereich: ------- #######
        connection_area = Frame(left_side, relief=RIDGE, borderwidth=2)
        connection_area.pack()

# --- Verbindungen ---
        label_single_car_connection = Label(
            connection_area,
            text="Erstes Auto - MAC Adresse",
            width=48,
            anchor="w"
        )
        label_single_car_connection.pack()

# --- MAC-Adressen der Fahrzeuge ---
        input_field = Label(connection_area, text=self.get_mac_first())
        input_field.pack()

        button_connect = Button(connection_area, text="Verbinden")
        button_connect.bind('<Button-1>', self.connect_first)
        button_connect.pack()

# ###### ------- Fahrzeugkontroll Bereich: ------- #######
        control_area = Frame(left_side, relief=RIDGE, borderwidth=2)
        control_area.pack()

# --- Geschwindigkeitskontrolle ---
        label_single_car_speed = Label(control_area, text="Geschwindigkeit", width=48, anchor="w")
        label_single_car_speed.pack()

        self.scale_single_car_speed = Scale(
            control_area,
            from_=1,
            to=6,
            orient=HORIZONTAL,
            length=200,
            command=self.handle_scale_first
        )
        self.scale_single_car_speed.pack()


# ###### ------- Platzhalter Bereich: ------- #######
        placeholder_area = Frame(left_side, relief=RIDGE, borderwidth=2, height=200)
        placeholder_area.pack()

# ###### ------- Button Bereich: ------- #######
        button_area = Frame(left_side, relief=RIDGE, borderwidth=2)
        button_area.pack()

# ###### ------- Rechte Seite ------- #######
        right_side = Frame(self, relief=RAISED, borderwidth=2)
        right_side.pack(side=LEFT, fill=Y)

        label_second_car = Label(
            right_side,
            text="Zweites Fahrzeug - MAC-Adresse",
            width=50,
            anchor="center",
            background="blue",
            relief=RAISED
        )
        label_second_car.pack()

        # ###### ------- Connection Bereich: ------- #######
        connection_area_second = Frame(right_side, relief=RIDGE, borderwidth=2)
        connection_area_second.pack()

        # --- Verbindungen ---
        label_second_car_connection = Label(
            connection_area_second,
            text="Zweites Auto - MAC Adresse",
            width=48,
            anchor="w"
        )
        label_second_car_connection.pack()

        # --- MAC-Adressen der Fahrzeuge ---
        second_label_field = Label(connection_area_second, text=self.get_mac_second())
        second_label_field.pack()

        second_button_connect = Button(connection_area_second, text="Verbinden")
        second_button_connect.bind('<Button-1>', self.connect_second)
        second_button_connect.pack()

        # ###### ------- Fahrzeugkontroll Bereich: ------- #######
        control_area_second = Frame(right_side, relief=RIDGE, borderwidth=2)
        control_area_second.pack()

        # --- Geschwindigkeitskontrolle ---
        label_second_car_speed = Label(control_area_second, text="Geschwindigkeit", width=48, anchor="w")
        label_second_car_speed.pack()

        self.scale_second_car_speed = Scale(
            control_area_second,
            from_=4,
            to=7,
            orient=HORIZONTAL,
            length=200,
            command=self.handle_scale_second
        )
        self.scale_second_car_speed.pack()

        # ###### ------- Platzhalter Bereich: ------- #######
        placeholder_area_second = Frame(right_side, relief=RIDGE, borderwidth=2, height=270)
        placeholder_area_second.pack()

        # ###### ------- Button Bereich: ------- #######
        second_button_area = Frame(right_side, relief=RIDGE, borderwidth=2)
        second_button_area.pack()

        # --- Start/Stop Button ---
        second_placeholder_button = Label(second_button_area, text="", width=33)
        second_placeholder_button.pack(side=LEFT)

        second_button_start = Button(second_button_area, text="Start")
        second_button_start.pack(side=LEFT)
        second_button_start.bind('<Button-1>', self.startCar)

        second_button_stop = Button(second_button_area, text="Stop")
        second_button_stop.pack(side=LEFT)
        second_button_stop.bind('<Button-1>', self.stopCar)


    def get_mac_first(self):
        return "ed:00:db:97:c2:de"

    def get_mac_second(self):
        return "fd:97:48:fb:a7:fe"

    def connect(mac):
        print(f"connecting to {mac}")
        be = FancyBackend(mac)
        if be.getOverdrive()._connected:
            print(f"connectied to {mac} [DONE]")
            return be
        else:
            print(f"{self.car_name} failed to connect to {mac} ")
            return None

    def connect_first(self, event):
        self.car_first = Gui.connect(self.get_mac_first())

    def connect_second(self, event):
        self.car_second = Gui.connect(self.get_mac_second())

    # min speed
    def handle_scale_first(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown disablen
        ## Connect anstossen
        ## Button soll Disconnect Button werden
        self.tour.setMinSpeed(event)
        self.scale_second_car_speed.config(_from=event)

    # max speed
    def handle_scale_second(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown disablen
        ## Connect anstossen
        self.tour.setMaxSpeed(event)
        self.scale_single_car_speed.config(to=event)

    def startCar(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown disablen
        ## Connect anstossen
        ## Button soll Disconnect Button werden
        self.tour.start()

    def stopCar(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown disablen
        ## Connect anstossen
        ## Button soll Disconnect Button werden
        self.tour.stop()
