from globals import Toplevel, Label, Button
from time import time


class Q3:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.geometry("500x250")
        self.root.title("This one should be simple")
        self.root.protocol("WM_DELETE_WINDOW", self.app.exit)

        Label(self.root, text="Violate the three second rule.").pack()
        self.button = Button(self.root, text="Drop Food")
        self.button.bind("<Button-1>", self.pressed)
        self.button.bind("<ButtonRelease-1>", self.unpressed)
        self.button.pack()

    def pressed(self, event):
        self.start = time()
        self.button.config(text="Pick Up Food")

    def unpressed(self, event):
        self.button.config(text="Drop Food")
        dt = time() - self.start
        if dt > 3:
            self.next()

    def next(self):
        print("you win")
        self.root.destroy()
        self.app.exit()


if __name__ == "__main__":
    from globals import Tk
    root = Tk()
    root.withdraw()
    Q3(root)
    root.mainloop()
