class Player():
    def __init__(self, name) -> None:
        self.name = name
        self._mark_mines= 0
        self._explod_mines = 0
        self.points = 0
    
    def add_points(self, points: int) -> None:
        self.points += points
    
    def subtract_points(self, points:int) -> None:
        self.points -= points
    
    def explod_mine(self):
        self._explod_mines += 1
    
    def mark_mine(self):
        self._mark_mines += 1
