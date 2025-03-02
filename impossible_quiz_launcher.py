from globals import Tk, Label, Button
from question_1 import Q1


class Quiz:
    def __init__(self):
        self.root = Tk()

        self.root.geometry("500x250")
        self.root.title("The Importance of Interpreting Instructions")
        Label(self.root, text="Welcome to Raphe's Quiz.\nTry to think outside the box,\nand use all the clues to find the solution.\nGood luck!\n"
        ).pack()
        Label(self.root, text="Before beginning, first get in control of the situation.").pack()
        self.root.bind("<Control_L>", self.control)
        self.root.bind("<Control_R>", self.control)
        Button(self.root, text="Begin", command=self.next).pack()
        self.bool = False
        self.root.mainloop()

    def control(self, event):
        self.bool = True

    def next(self):
        if self.bool:
            self.root.withdraw()
            Q1(self.root)


if __name__ == "__main__":
    q = Quiz()
