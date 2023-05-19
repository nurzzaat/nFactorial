import tkinter as tr
from random import shuffle

class Saper:
    window = tr.Tk()
    row = 10
    col = 10
    mine = 10
    buttons = []

    def __init__(self):
        self.buttons = []
        count = 1
        for i in range(Saper.row):
            temp = []
            for j in range(Saper.col):
                button = Saper_Button(Saper.window, x=i, y=j, number=count, width=3, font='Arial 13 bold')
                temp.append(button)
                count += 1
            self.buttons.append(temp)

    def start(self):
        self.create_btn()
        self.insert_mine()
        Saper.window.mainloop()

    def create_btn(self):
        for i in range(Saper.row):
            for j in range(Saper.col):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    @staticmethod
    def place_of_mines():
        index_list = list(range(1, Saper.row * Saper.col + 1))
        print(index_list)
        shuffle(index_list)
        return index_list[:Saper.mine]

    def insert_mine(self):
        index_mine = self.place_of_mines()
        for btns in self.buttons:
            for btn in btns:
                if btn.number in index_mine:
                    print(btn.number)
                    btn.is_mine = True


class Saper_Button(tr.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(Saper_Button, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False


game = Saper()
game.start()