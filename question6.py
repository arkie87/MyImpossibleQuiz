
from globals import Toplevel, Label, Button, Entry


class Q6:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.geometry("500x250")
        self.root.title("Hit no")
        self.root.protocol("WM_DELETE_WINDOW", self.app.exit)

        button = MyButton(self.root, text="No", x=0, y=100, command=lambda x: None)
        button = MyButton(self.root, text="No", x=50, y=200, command=lambda x: None)
        button = MyButton(self.root, text="No", x=150, y=200, command=lambda x: None)
        button = MyButton(self.root, text="No", x=150, y=50, command=lambda x: None)

        button = MyButton(self.root, text="No", x=200, y=200, command=lambda x: None)
        button = MyButton(self.root, text="No", x=50, y=150, command=lambda x: None)
        button = MyButton(self.root, text="No", x=150, y=150, command=lambda x: None)
        button = MyButton(self.root, text="No", x=150, y=100, command=lambda x: None)

        button = MyButton(self.root, text="no", x=50, y=50, command=self.next)

    def next(self, bool):
        if bool:
            print("you win")
            self.root.destroy()
            self.app.exit()



class MyButton:
    def __init__(self, root, text, x, y, command):
        self.button = Button(root, text=text)
        self.x, self.y = x, y
        self.button.bind("<Enter>", self.forget)
        self.button.bind("<Leave>", self.place)
        self.button.bind("<Return>", lambda b: command(self.bool))
        self.place(None)

    def place(self, event):
        self.bool = True
        self.button.place(x=self.x, y=self.y)

    def forget(self, event):
        self.bool = False
        self.button.place_forget()



if __name__ == "__main__":
    from globals import App
    app = App()
    Q6(app)
    app.root.mainloop()
