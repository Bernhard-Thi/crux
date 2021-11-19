from tkinter import BOTH, LEFT, RAISED, RIGHT, Y, Scale, HORIZONTAL, Button, IntVar, Checkbutton
from tkinter.ttk import Frame, Label


class Gui(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("crux")
        self.pack(fill=BOTH, expand=True)

        # Linke Seite:
        leftSide = Frame(self, relief=RAISED, borderwidth=2)
        leftSide.pack(side=LEFT, fill=Y)

        labelSingleCar = Label(leftSide, text="Einzelfahrzeug", width=50, anchor="center", background="lightblue")
        labelSingleCar.pack(padx=5, pady=5)

        # Geschwindigkeitskontrolle
        labelSingleCarSpeed = Label(leftSide, text="Geschwindigkeit", width=50, anchor="center")
        labelSingleCarSpeed.pack(padx=5, pady=5)

        scaleSingleCarSpeed = Scale(
            leftSide,
            from_=0,
            to=1000,
            orient=HORIZONTAL,
            length=200
        )
        scaleSingleCarSpeed.pack(padx=5, pady=5)

        # Verhalten
        labelSingleCarHandling = Label(leftSide, text="Verhalten des Fahrzeuges", width=50, anchor="center")
        labelSingleCarHandling.pack(padx=5, pady=5)

        option1 = IntVar()
        checkSingleCarOpt1 = Checkbutton(leftSide, text="Rechts fahren", variable=option1, width=50, anchor="w")
        checkSingleCarOpt1.pack()

        option2 = IntVar()
        checkSingleCarOpt2 = Checkbutton(leftSide, text="Möglichst schnell", variable=option2, width=50, anchor="w")
        checkSingleCarOpt2.pack()

        option3 = IntVar()
        checkSingleCarOpt3 = Checkbutton(leftSide, text="Möglichst ohne stoppen", variable=option3, width=50, anchor="w")
        checkSingleCarOpt3.pack()

        # Start/Stop Button
        buttonStart = Button(
            leftSide,
            text="Start"
        )
        buttonStart.pack()

        buttonStop = Button(
            leftSide,
            text="Stop"
        )
        buttonStop.pack()

        # Rechte Seite
        rightSide = Frame(self, relief=RAISED, borderwidth=2)
        rightSide.pack(side=RIGHT, fill=Y)

        labelMultipleCar = Label(rightSide, text="Schwarm", width=50, anchor="center", background="lightgreen")
        labelMultipleCar.pack(padx=5, pady=5)

        labelMultipleCarSpeed = Label(rightSide, text="Geschwindigkeit", width=50, anchor="center")
        labelMultipleCarSpeed.pack(padx=5, pady=5)

        scaleSingleCarSpeed = Scale(
            rightSide,
            from_=0,
            to=1000,
            orient=HORIZONTAL,
            length=200
        )
        scaleSingleCarSpeed.pack(padx=5, pady=5)