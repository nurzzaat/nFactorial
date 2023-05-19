import tkinter as tr


class Saper:
    window = tr.Tk()
    row = 10
    col = 10
    buttons = []

    def __init__(self):
        for i in range(Saper.row):
            temp = []
            for j in range(Saper.col):
                button = Button(Saper.window, x=i, y=j, width=3, font='Arial 13 bold')
                temp.append(button)
            Saper.buttons.append(temp)

    def start(self):
        self.create_btn()
        Saper.window.mainloop()

    def create_btn(self):
        for i in range(Saper.row):
            for j in range(Saper.col):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)


class Button(tr.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(Button, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number

game = Saper()
game.start()