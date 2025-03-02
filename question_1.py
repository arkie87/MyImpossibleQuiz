from globals import Toplevel, Label, Button


class Q1:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.title("Maximize Your Range of Thought")
        Label(self.root, text="In this question, you need to maximize your range of thought so that you can discover new things").place(x=0,y=0)
        button = Button(self.root, text="New Things", command=self.next, takefocus=0).place(x=1000, y=1000)

        self.root.geometry("400x200")


    def next(self):
        print("you win")
        self.root.destroy()
        self.app.destroy()


if __name__ == "__main__":
    from globals import Tk
    root = Tk()
    root.withdraw()
    Q1(root)
    root.mainloop()
