import tkinter as tk
from sys import exit
from tkinter import messagebox
from random import choice
from source.box import Box

def return_new_function(func, *params):
    def new_func():
        func(*params)
    return new_func


class Game:
    def __init__(self, root, shift_element, players:list, rows=5, colums=5, mines=8) -> None:
        self.__root = root
        self.__shift_element = shift_element
        self.__players = players
        self.__player_index = 0
        self.__boxes = []
        self._rows = rows
        self._columns = colums
        self.mines = mines
        self.mines_found = 0
    
    @property
    def rows(self, rows: int):
        if not isinstance(rows, int):
            raise TypeError("The rows property must be an integer")
        elif not (0 < rows < 11):
            raise ValueError("The rows property must be between 1 - 10")
        self._rows = rows
    
    @rows.setter
    def rows(self):
        return self._rows
    
    @property
    def columns(self, columns: int):
        if not isinstance(columns, int):
            raise TypeError("The columns property must be an integer")
        elif not (0 < columns < 11):
            raise ValueError("The columns property must be between 1 - 10")
        self._columns = columns
    
    @columns.setter
    def columns(self):
        return self._columns
    
    def get_player(self):
        return self.__players[self.__player_index]
    
    def next_player(self):
        self.__player_index = (self.__player_index + 1) % len(self.__players)
    
    def click_box(self, box: Box):
        if box.clicked:
            return
        
        player = self.get_player()

        if box.active:
            box.update("💣")
            print(f"{player.name} Boom!")
            player.mines_found += 1
            self.mines_found += 1
        else:
            box.update()
            
        box.clicked = True
        self.next_player()

        if self.mines_found >= self.mines:
            result = ""
            for player in self.__players:
                result += f"{player.name}: Mines Found: {player.mines_found}\n"
            messagebox.showinfo("GAME OVER", result)
            exit()
        self.update_shift()
    
    def update_shift(self):
        self.__shift_element.config(text=f"Player: {self.get_player().name}")
    
    def start(self):
        game_root = tk.Frame(self.__root)
        game_root.pack()

        # create boxes
        for i in range(self._rows):
            row = []
            row_element = tk.Frame(game_root)
            for j in range(self._columns):
                button = tk.Button(row_element, font=("Helvetica", 20, "bold"), width=5)
                box = Box(button)
                button.config(command=return_new_function(self.click_box, box))
                box.pack()
                row.append(box)
            self.__boxes.append(row)
            row_element.pack()
        
        # select random boxes actives
        mines_counter = 0
        while mines_counter < self.mines:
            random_row = choice(self.__boxes)
            random_box = choice(random_row)
            if not random_box.active:
                random_box.active = True
                mines_counter += 1
        
        # calculate adjacent mines
        for i in range(self._rows):
            for j in range(self._columns):
                adjacent_mines = 0
                if i > 0 and self.__boxes[i-1][j].active:
                    adjacent_mines += 1
                if i < self._rows - 1 and self.__boxes[i+1][j].active:
                    adjacent_mines += 1
                if j > 0 and self.__boxes[i][j-1].active:
                    adjacent_mines += 1
                if j < self._columns - 1 and self.__boxes[i][j+1].active:
                    adjacent_mines += 1

                self.__boxes[i][j].value = adjacent_mines