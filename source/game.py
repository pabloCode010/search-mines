import tkinter as tk
from sys import exit
from tkinter import messagebox
from random import choice
from source.mine import Mine

def return_new_function(func, *params):
    def new_func(*args):
        func(*params)
    return new_func


class Game:
    def __init__(self, root, shift_element, players:list, rows=5, colums=5, mines=8) -> None:
        self.__root = root
        self.__shift_element = shift_element
        self.players = players
        self.__player_index = 0
        self.__mines = []
        # self.is_first_click = True
        self.rows = rows
        self.columns = colums
        self.mines = mines
        self.mines_found = 0
    
    def get_player(self):
        return self.players[self.__player_index]
    
    def next_player(self):
        self.__player_index = (self.__player_index + 1) % len(self.players)
    
    def update_shift(self):
        player = self.get_player()
        self.__shift_element.config(text=f"Player: {player.name}               Points: {player.points}")
    
    def check_game_over(self):
        if self.mines_found >= self.mines:
            result = ""
            for player in self.players:
                result += f"{player.name}: {player.points}\n"
            messagebox.showinfo("GAME OVER", result)
            exit()

    def active_random_mines(self):
        # select random boxes actives
        mines_counter = 0
        while mines_counter < self.mines:
            random_row = choice(self.__mines)
            random_box = choice(random_row)
            if not random_box.clicked and not random_box.active:
                random_box.active = True
                mines_counter += 1
        
    def calculate_adjacent_mines(self):
        for i in range(self.rows):
            for j in range(self.columns):
                adjacent_mines = 0
                if i > 0 and j > 0 and self.__mines[i-1][j-1].active:
                    adjacent_mines += 1
                if i > 0 and self.__mines[i-1][j].active:
                    adjacent_mines += 1
                if i > 0 and j < self.columns - 1 and self.__mines[i-1][j+1].active:
                    adjacent_mines += 1
                if j < self.columns - 1 and self.__mines[i][j+1].active:
                    adjacent_mines += 1
                if j < self.columns - 1 and i < self.rows -1 and self.__mines[i+1][j+1].active:
                    adjacent_mines += 1
                if i < self.rows - 1 and self.__mines[i+1][j].active:
                    adjacent_mines += 1
                if i < self.rows - 1 and j > 0 and self.__mines[i+1][j-1].active:
                    adjacent_mines += 1
                if j > 0 and self.__mines[i][j-1].active:
                    adjacent_mines += 1

                self.__mines[i][j].adjacent_mines = adjacent_mines
    
    def start(self):
        game_root = tk.Frame(self.__root)
        game_root.pack()

        for i in range(self.rows):
            row = []
            row_element = tk.Frame(game_root)
            for j in range(self.columns):
                button = tk.Button(row_element, font=("Helvetica", 20, "bold"), width=5)
                mine = Mine(button)
                button.config(command=return_new_function(mine.click_left, self))
                button.bind("<Button-3>", return_new_function(mine.click_right, self))
                mine.pack()
                row.append(mine)
            self.__mines.append(row)
            row_element.pack()
        
        self.active_random_mines()
        self.calculate_adjacent_mines()
        