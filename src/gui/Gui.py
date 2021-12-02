from tkinter import Tk, BOTH, LEFT, RAISED, RIGHT, Y, Scale, HORIZONTAL, Button, IntVar, Checkbutton, OptionMenu, \
    StringVar
from tkinter.ttk import Frame, Label


def main():
    root = Tk()
    root.geometry("800x600")
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

        label_single_car = Label(left_side, text="Einzelfahrzeug", width=50, anchor="center", background="lightblue")
        label_single_car.pack(padx=5, pady=5)

# --- Verbindungen ---
        label_single_car_connection = Label(left_side, text="MAC-Adresse", width=50, anchor="w")
        label_single_car_connection.pack(padx=5, pady=5)

# --- MAC-Adressen der Fahrzeuge ---
        mac_list = [
            "ed:00:db:97:c2:de",
            "fd:97:48:fb:a7:fe"
        ]

        chosen_value = StringVar(self)
        chosen_value.set(mac_list[0])
        input_field = OptionMenu(left_side, chosen_value, *mac_list)
        input_field.pack()

        button_connect = Button(left_side, text="Verbinden")
        button_connect.bind('<Button-1>', self.connect)
        button_connect.pack()

# --- Geschwindigkeitskontrolle ---
        label_single_car_speed = Label(left_side, text="Geschwindigkeit", width=50, anchor="w")
        label_single_car_speed.pack(padx=5, pady=5)

        scale_single_car_speed = Scale(
            left_side,
            from_=0,
            to=1000,
            orient=HORIZONTAL,
            length=200
        )
        scale_single_car_speed.pack(padx=5, pady=5)

# --- Batterie Anzeige ---
        label_single_car_battery = Label(left_side, text="Batterieanzeige", width=50, anchor="w")
        label_single_car_battery.pack(padx=5, pady=5)

        label_single_car_battery_status = Label(left_side, text="xxx %", width=50, anchor="center")
        label_single_car_battery_status.pack()

# --- Batterie Styles ---
        label_single_car_battery_status_view = Label(left_side, text="", width=5, background="yellow")
        label_single_car_battery_status_view.pack()

# ---  Verhalten ---
        label_single_car_handling = Label(left_side, text="Verhalten des Fahrzeuges", width=50, anchor="w")
        label_single_car_handling.pack(padx=5, pady=5)

        option1 = IntVar()
        check_single_car_opt1 = Checkbutton(left_side, text="Rechts fahren", variable=option1, width=50, anchor="w")
        check_single_car_opt1.pack()

        option2 = IntVar()
        check_single_car_opt2 = Checkbutton(left_side, text="Möglichst schnell", variable=option2, width=50, anchor="w")
        check_single_car_opt2.pack()

        option3 = IntVar()
        check_single_car_opt3 = Checkbutton(
            left_side,
            text="Möglichst ohne stoppen",
            variable=option3,
            width=50,
            anchor="w"
        )
        check_single_car_opt3.pack()

# --- Start/Stop Button ---
        button_start = Button(left_side, text="Start")
        button_start.pack()

        button_stop = Button(left_side, text="Stop")
        button_stop.pack()

# ###### ------- Rechte Seite ------- #######
        right_side = Frame(self, relief=RAISED, borderwidth=2)
        right_side.pack(side=RIGHT, fill=Y)

        label_multiple_car = Label(right_side, text="Schwarm", width=50, anchor="center", background="lightgreen")
        label_multiple_car.pack(padx=5, pady=5)

# --- Geschwindigkeitskontrolle Schwarm ---

        label_multiple_car_speed = Label(right_side, text="Geschwindigkeit", width=50, anchor="center")
        label_multiple_car_speed.pack(padx=5, pady=5)

        scale_single_car_speed = Scale(
            right_side,
            from_=0,
            to=1000,
            orient=HORIZONTAL,
            length=200
        )
        scale_single_car_speed.pack(padx=5, pady=5)

    def connect(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown disablen
        ## Connect anstoßen
        ## Button soll Disconnect Button werden
        print("comming soon")

    def disconnect(self, event):
        ## Was soll diese Funktion machen?
        ## Dropdown enablen
        ## Fahrzeuge disconnecten
        ## Button soll Connect Button werden
        print("comming soon")

    def check_battery(self):
        ## Was soll diese Funktion machen?
        ## Batterie Status überprüfen
        ## xxx des label_single_car_battery_status in 038% umwandeln
        ## label_single_car_battery_status_view background nach Batteriestand färben < 10% => rot
        ## Funktion soll während der Fahrzeug intervallmäßig laufen, wenn auf Startbutton gedrück wurde
        print("test")

    def changeSpeed(self):
        ## Diese Funktion soll nach loslassen des Reglers den Wert der Scale auslesen
        ## Außerdem soll sie die Geschwindigkeit des ausgewählten Fahrzeug (siehe Dropdown) steuern
        ## optionMenu (input_field)
        print("coming soon")