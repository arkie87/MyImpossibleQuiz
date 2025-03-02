from globals import Toplevel, Label, Button


class Q2:
    def __init__(self, app):
        self.app = app
        self.root = Toplevel()
        self.root.title("Click All of the Above")
        Label(self.root, text="The questions obey the same basic rules.").pack()
        Label(self.root, text="Sometimes, more than one answer is right.").pack()
        Label(self.root, text="For instance, in this question, all of the above are correct").pack()
        Label(self.root, text="Fe is...").pack()

        self._exam = Button(self.root, text="An Exam", command=self.exam)
        self._note = Button(self.root, text="A Musical Note", command=self.note)
        self._metal = Button(self.root, text="A Type of Metal", command=self.metal)
        self._game = Button(self.root, text="A game on steam", command=self.game)

        self._exam.pack()
        self._note.pack()
        self._metal.pack()
        self._game.pack()

        Button(self.root, text="All of the above", command=self.reset).pack()

        self.root.geometry("500x250")
        self.reset()

    def exam(self):
        self.bools[0] = True
        self._exam.config(relief="sunken")
        self.next()

    def note(self):
        self.bools[1] = True
        self._note.config(relief="sunken")
        self.next()

    def metal(self):
        self.bools[2] = True
        self._metal.config(relief="sunken")
        self.next()

    def game(self):
        self.bools[3] = True
        self._game.config(relief="sunken")
        self.next()

    def reset(self):
        self._exam.config(relief="raised")
        self._note.config(relief="raised")
        self._metal.config(relief="raised")
        self._game.config(relief="raised")
        self.bools = [False, False, False, False]


    def next(self):
        if all(self.bools):
            print("you win")
            self.root.destroy()
            self.app.destroy()


if __name__ == "__main__":
    from globals import Tk
    root = Tk()
    root.withdraw()
    Q2(root)
    root.mainloop()
