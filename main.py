import tkinter as tr
from random import shuffle
from tkinter.messagebox import showinfo

colors = {
    1: 'black',
    2: 'orange',
    3: 'blue',
    4: 'red'
}


class Saper_Button(tr.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(Saper_Button, self).__init__(master, *args, **kwargs)
        self.y = y
        self.x = x
        self.number = number
        self.is_mine = False
        self.count_mine = 0
        self.is_open = False


class Saper:
    window = tr.Tk()
    row = 10
    col = 10
    mine = 10
    total = row * col - mine
    buttons = []
    game_over = False
    first_click = True

    def start(self):
        self.create_btn()
        Saper.window.mainloop()

    def __init__(self):
        for i in range(Saper.row + 2):
            temp = []
            for j in range(Saper.col + 2):
                button = Saper_Button(Saper.window, x=i, y=j, width=3, font='Arial 14 bold')
                button.config(command=lambda btn=button: self.click(btn))
                temp.append(button)
            Saper.buttons.append(temp)

    def click(self, clicked_btn: Saper_Button):

        if Saper.game_over:
            return

        if Saper.first_click:
            self.insert_mine(clicked_btn.number)
            self.count_mines()
            Saper.first_click = False

        if clicked_btn.is_mine:
            clicked_btn.config(text="*", background='red', disabledforeground='black')
            clicked_btn.is_open = True
            Saper.total -= 1
            if Saper.total == 0:
                showinfo('Congratulations', 'You won!')
                Saper.window.quit()

            Saper.game_over = True
            showinfo('Game over', 'Game over')
            for i in range(1, Saper.row + 1):
                for j in range(1, Saper.col + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'
        else:
            color = colors.get(clicked_btn.count_mine)
            if clicked_btn.count_mine:
                clicked_btn.config(text=clicked_btn.count_mine, disabledforeground=color)
                clicked_btn.is_open = True
                Saper.total -= 1
                if Saper.total == 0:
                    showinfo('Congratulations', 'You won!')
                    Saper.window.quit()
            else:
                self.first_search(clicked_btn)
        clicked_btn.config(state='disabled')
        clicked_btn.config(relief=tr.SUNKEN)

    def create_btn(self):
        count = 1
        for i in range(1, Saper.row + 1):
            for j in range(1, Saper.col + 1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j)
                count += 1

    def first_search(self, btn: Saper_Button):
        queue = [btn]
        while queue:

            current = queue.pop()
            color = colors.get(current.count_mine)
            if current.count_mine:
                current.config(text=current.count_mine, disabledforeground=color)
            else:
                current.config(text='', disabledforeground=color)
            current.config(state='disabled')
            current.config(relief=tr.SUNKEN)
            current.is_open = True
            Saper.total -= 1
            if Saper.total == 0:
                showinfo('Congratulations', 'You won!')
                Saper.window.quit()

            if current.count_mine == 0:
                dx, dy = current.x, current.y
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        next_btn = self.buttons[x + dx][y + dy]
                        if not next_btn.is_open and 1 <= next_btn.x <= Saper.row and \
                                1 <= next_btn.y <= Saper.col and next_btn not in queue:
                            queue.append(next_btn)

    def count_mines(self):

        for i in range(1, Saper.row + 1):
            for j in range(1, Saper.col + 1):
                btn = self.buttons[i][j]
                count_mine = 0
                if not btn.is_mine:
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            neighbor = self.buttons[i + x][j + y]
                            if neighbor.is_mine:
                                count_mine += 1
                btn.count_mine = count_mine

    @staticmethod
    def place_of_mines(exclude_num):
        index_list = list(range(1, Saper.row * Saper.col + 1))
        index_list.remove(exclude_num)
        shuffle(index_list)
        return index_list[:Saper.mine]

    def insert_mine(self, number: int):
        index_mine = self.place_of_mines(number)
        for i in range(1, Saper.row + 1):
            for j in range(1, Saper.col + 1):
                btn = self.buttons[i][j]
                if btn.number in index_mine:
                    btn.is_mine = True


game = Saper()
game.start()
