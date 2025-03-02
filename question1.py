from globals import App, Toplevel, Label, Button
from question2 import Q2


class Q1:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()

        self.root.geometry("500x250")
        self.root.title("The Importance of Interpreting Instructions")
        Label(self.root, text="Welcome to Raphe's Quiz.\nTry to think outside the box,\nand use all the clues to find the solution.\nGood luck!\n"
        ).pack()
        Label(self.root, text="Before beginning, first get in control of the situation.").pack()
        self.button = Button(self.root, text="Begin")
        self.button.bind("<Control-Button-1>", self.next)
        self.button.pack()
        self.root.mainloop()

    def next(self, event):
        self.root.destroy()
        Q2(self.app)


if __name__ == "__main__":
    from globals import App
    app = App()
    Q1(app)
    app.root.mainloop()
