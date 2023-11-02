class Mine:
    def __init__(self, button, adjacent_mines=0, active=False) -> None:
        self.adjacent_mines = adjacent_mines
        self.active = active
        self.button = button
        self.clicked = False
    
    def update(self, text_update=None) -> None:
        if text_update is None:
            self.button.config(text=f"{self.adjacent_mines}")
        else:
            self.button.config(text=text_update)
    
    def pack(self) -> None:
        self.button.pack(side="left", padx=5, pady=5)
    
    def click_left(self, game) -> None:
        if self.clicked:
            return None

        player = game.get_player()
        if self.active:
            self.update("💣")
            player.explod_mine()
            player.subtract_points(10)
            game.mines_found += 1
            print(f"{player.name} Boom! -10 points")
        else:
            self.update()
            player.add_points(5)
            print(f"{player.name} +5 points")
        
        self.clicked = True
        game.next_player()

        game.check_game_over()
        game.update_shift()
    
    def click_right(self, game):
        if self.clicked:
            return
        
        player = game.get_player()
        if self.active:
            self.update("🚩")
            player.add_points(10)
            player.mark_mine()
            game.mines_found += 1
            print(f"{player.name} Find Mine! +10 points")
        else:
            self.update()
            print(f"{player.name} That wasn't a bomb! +0 points")
            
        self.clicked = True
        game.next_player()

        game.check_game_over()
        game.update_shift()