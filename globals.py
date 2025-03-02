from tkinter import Tk, Toplevel, Button, Entry, Label


class App: 
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

    def exit(self):
        self.root.destroy()
