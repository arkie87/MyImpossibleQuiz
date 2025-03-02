from globals import Tk, Label, Button
from question1 import Q1


class Quiz:
    def __init__(self):
        self.root = Tk()

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
        self.root.withdraw()
        Q1(self)

    def exit(self):
        self.root.destroy()



if __name__ == "__main__":
    q = Quiz()
