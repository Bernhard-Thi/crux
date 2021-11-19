from tkinter import Tk
from Gui import Gui

def main():
    root = Tk()
    root.geometry("800x600")
    app=Gui()
    root.mainloop()

if __name__ == '__main__':
    main()