class Box:
    def __init__(self, element, value=0, active=False) -> None:
        self.__value = value
        self.__active = active
        self.__element = element
        self.__clicked = False
    
    @property
    def value(self) -> int:
        return self.__value
    
    @property
    def active(self) -> bool:
        return self.__active

    @value.setter
    def value(self, value: int):
        if not isinstance(value, int):
            raise TypeError("The value property must be an integer")
        self.__value = value

    @active.setter
    def active(self, active: bool):
        if not isinstance(active, bool):
            raise TypeError("The active property must be a boolean")
        self.__active = active
    
    @property
    def clicked(self):
        return self.__clicked
    
    @clicked.setter
    def clicked(self, clicked: bool):
        if not isinstance(clicked, bool):
            raise TypeError("The clicked property must be a boolean")
        self.__clicked = clicked

    
    def update(self, text_update=None) -> None:
        text_update = text_update if text_update else f"{self.__value}"
        self.__element.config(text=text_update)
    
    def pack(self) -> None:
        self.__element.pack(side="left", padx=5, pady=5)