from globals import Toplevel, Label, Button
from question_2 import Q2


class Q1:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.title("Your Range of Thought")
        Label(self.root, text="This lesson is to teach you how to\nmaximize your range of thought so\nthat you can discover new things").place(x=0,y=0)
        button = Button(self.root, text="New Things", command=self.next, takefocus=0).place(x=1000, y=1000)

        self.root.geometry("500x250")


    def next(self):
        Q2(self.app)
        self.root.destroy()


if __name__ == "__main__":
    from globals import Tk
    root = Tk()
    root.withdraw()
    Q1(root)
    root.mainloop()
