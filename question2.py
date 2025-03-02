from globals import Toplevel, Label, Button
from question3 import Q3


class Q2:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.geometry("500x250")
        self.root.title("Your Range of Thought")
        self.root.protocol("WM_DELETE_WINDOW", self.app.exit)

        Label(self.root, text="This lesson is to teach you how to\nmaximize your range of thought so\nthat you can discover new things").place(x=0,y=0)
        button = Button(self.root, text="New Things", command=self.next, takefocus=0).place(x=1000, y=1000)

    def next(self):
        self.root.destroy()
        Q3(self.app)


if __name__ == "__main__":
    from globals import App
    app = App()
    Q2(app)
    app.root.mainloop()
