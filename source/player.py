class Player():
    def __init__(self, name) -> None:
        self.__name = name
        self.__mines_found = 0
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("The name property must be a string")
        self.__name = name
    
    @property
    def mines_found(self):
        return self.__mines_found
    
    @mines_found.setter
    def mines_found(self, mines_found: int):
        if not isinstance(mines_found, int):
            raise TypeError("The mines_found property must be an integer")
        self.__mines_found = mines_found