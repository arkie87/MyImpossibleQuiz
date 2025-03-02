from globals import Toplevel, Label, Button, Entry
from question6 import Q6


class Q5:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.geometry("500x250")
        self.root.title("What's The Number?")
        self.root.protocol("WM_DELETE_WINDOW", self.app.exit)

        Label(self.root, text="Number 1-1000:").pack()
        self.entry = Entry(self.root)
        self.entry.pack()
        Button(self.root, text="Submit", command=self.next).pack()

    def next(self):
        if not self.entry.get() == "-999": 
            self.entry.delete(0, "end")
        else:
            self.root.destroy()
            Q6(self.app)


if __name__ == "__main__":
    from globals import App
    app = App()
    Q5(app)
    app.root.mainloop()
