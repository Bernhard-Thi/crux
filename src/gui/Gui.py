from tkinter import Tk, BOTH, LEFT, RAISED, RIDGE, RIGHT, Y, Scale, HORIZONTAL, Button, OptionMenu, \
    StringVar
from tkinter.ttk import Frame, Label, Entry


def main():
    root = Tk()
    root.geometry("800x525")
    app = Gui()
    root.mainloop()



class Gui(Frame):
#    def __init__(self, _backend):
    def __init__(self):
        super().__init__()
#        self.backend = _backend
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
            background="lightblue",
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
        mac_list = [
            "ed:00:db:97:c2:de",
            "fd:97:48:fb:a7:fe"
        ]

        chosen_value = StringVar(self)
        chosen_value.set(mac_list[0])
        input_field = OptionMenu(connection_area, chosen_value, *mac_list)
        input_field.pack()

        button_connect = Button(connection_area, text="Verbinden")
        button_connect.bind('<Button-1>', self.connect)
        button_connect.pack()

# ###### ------- Fahrzeugkontroll Bereich: ------- #######
        control_area = Frame(left_side, relief=RIDGE, borderwidth=2)
        control_area.pack()

# --- Geschwindigkeitskontrolle ---
        label_single_car_speed = Label(control_area, text="Geschwindigkeit", width=48, anchor="w")
        label_single_car_speed.pack()

        scale_single_car_speed = Scale(
            control_area,
            from_=0,
            to=1000,
            orient=HORIZONTAL,
            length=200
        )
        scale_single_car_speed.pack()

# --- Batterie Anzeige ---
        label_single_car_battery = Label(control_area, text="Batterieanzeige", width=48, anchor="w")
        label_single_car_battery.pack()

        label_single_car_battery_status = Label(control_area, text="xxx %", width=48, anchor="center")
        label_single_car_battery_status.pack()

# --- Batterie Styles ---
        label_single_car_battery_status_view = Label(control_area, text="", width=5, background="yellow")
        label_single_car_battery_status_view.pack()

# ###### ------- Platzhalter Bereich: ------- #######
        placeholder_area = Frame(left_side, relief=RIDGE, borderwidth=2, height=200)
        placeholder_area.pack()

# ###### ------- Button Bereich: ------- #######
        button_area = Frame(left_side, relief=RIDGE, borderwidth=2)
        button_area.pack()

# --- Start/Stop Button ---
        placeholder_button = Label(button_area, text="", width=33)
        placeholder_button.pack(side=LEFT)

        button_start = Button(button_area, text="Start")
        button_start.pack(side=LEFT)

        button_stop = Button(button_area, text="Stop")
        button_stop.pack(side=LEFT)

# ###### ------- Rechte Seite ------- #######
        right_side = Frame(self, relief=RAISED, borderwidth=2)
        right_side.pack(side=LEFT, fill=Y)

        label_second_car = Label(
            left_side,
            text="Einzelfahrzeug",
            width=50,
            anchor="center",
            background="lightblue",
            relief=RAISED
        )
        label_second_car.pack()

        # ###### ------- Connection Bereich: ------- #######
        connection_area_second = Frame(left_side, relief=RIDGE, borderwidth=2)
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
        second_label_field = Label(connection_area, text="fd:97:48:fb:a7:fe")
        second_label_field.pack()

        second_button_connect = Button(connection_area, text="Verbinden")
        second_button_connect.bind('<Button-1>', self.connect)
        second_button_connect.pack()

        # ###### ------- Fahrzeugkontroll Bereich: ------- #######
        second_control_area = Frame(right_side, relief=RIDGE, borderwidth=2)
        second_control_area.pack()

        # --- Geschwindigkeitskontrolle ---
        label_second_car_speed = Label(control_area_second, text="Geschwindigkeit", width=48, anchor="w")
        label_second_car_speed.pack()

        scale_second_car_speed = Scale(
            control_area,
            from_=0,
            to=1000,
            orient=HORIZONTAL,
            length=200
        )
        scale_second_car_speed.pack()

        # --- Batterie Anzeige ---
        label_second_car_battery = Label(control_area_second, text="Batterieanzeige", width=48, anchor="w")
        label_second_car_battery.pack()

        label_second_car_battery_status = Label(control_area_second, text="xxx %", width=48, anchor="center")
        label_second_car_battery_status.pack()

        # --- Batterie Styles ---
        label_second_car_battery_status_view = Label(control_area_second, text="", width=5, background="yellow")
        label_second_car_battery_status_view.pack()

        # ###### ------- Platzhalter Bereich: ------- #######
        placeholder_area_second = Frame(right_side, relief=RIDGE, borderwidth=2, height=200)
        placeholder_area_second.pack()

        # ###### ------- Button Bereich: ------- #######
        second_button_area = Frame(right_side, relief=RIDGE, borderwidth=2)
        second_button_area.pack()

        # --- Start/Stop Button ---
        second_placeholder_button = Label(second_button_area, text="", width=33)
        second_placeholder_button.pack(side=LEFT)

        second_button_start = Button(second_button_area, text="Start")
        second_button_start.pack(side=LEFT)

        second_button_stop = Button(second_button_area, text="Stop")
        second_button_stop.pack(side=LEFT)


    def add_mac(self, event):
        ## Was soll diese Funktion machen?
        ## entry_connection_add auslesen und in mac_list einfuegen
        print(f"add_mac {event}")

    def connect(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown disablen
        ## Connect anstossen
        ## Button soll Disconnect Button werden
        print(f"connect {event}")

    def disconnect(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown enablen
        ## Fahrzeuge disconnecten
        ## Button soll Connect Button werden
        print(f"disconnect {event}")

    def check_battery(self):
        ## Was soll diese Funktion machen?
        ## Batterie Status ueberpruefen
        ## xxx des label_single_car_battery_status in 038% umwandeln
        ## label_single_car_battery_status_view background nach Batteriestand faerben < 10% => rot
        ## Funktion soll waehrend der Fahrzeug intervallmaessig laufen, wenn auf Startbutton gedrueckt wurde
        print("check_battery")

    def changeSpeed(self):
        ## Diese Funktion soll nach loslassen des Reglers den Wert der Scale auslesen
        ## Ausserdem soll sie die Geschwindigkeit des ausgewaehlten Fahrzeug (siehe Dropdown) steuern
        ## optionMenu (input_field)
        print("changeSpeed")
