#https://github.com/pabloCode010

import tkinter as tk
from source.game import Game
from source.player import Player
from random import randint

# rows = int(input("Rows: "))
# columns = int(input("Columns: "))
# mines = int(input("Mines: "))

# length_players = int(input("Players: "))
# players = [Player(input(f"Name Player {i}: ")) for i in range(length_players)]

rows = columns = 6
mines = 15
players = [Player("John Doe"), Player("Torvalds")]

# more players
# players = [Player("John Doe"), Player("Torvalds"), Player("Pablo"), Player("Arturo")]

root = tk.Tk()
title = tk.Label(root, text="Search Mines 💣", font=("Helvetica", 25, "bold"), padx=10, pady=10)
title.pack(side="top", anchor="w")

shift = tk.Label(root, font=("Helvetica", 15, "bold"))
shift.pack()

game = Game(root, shift, players, rows, columns, mines)
game.start()
game.update_shift()

root.mainloop()