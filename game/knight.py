class Knight:

    def __init__(self, x, y, defence, attack, colour) -> None:
        self.x = x
        self.y = y
        self.defence = defence
        self.attack = attack
        self.item = None
        self.dead = False
        self.drowned = False
        self.colour = colour
    
    def get_status(self):
        if self.drowned:
            return "DROWNED"
        if self.dead:
            return "DEAD"
        return "LIVE"
    
    def get_position(self):
        if self.x == None or self.y == None:
            return None
        return [self.x,self.y]
    
    def __get_item(self):
        if self.item != None:
            return self.item.name
        return None

    def get_attributes(self):
        return [self.get_position(), self.get_status(),self.__get_item(),self.attack,self.defence]

    def __str__(self) -> str:
        return f"\"{self.colour}\" : [{self.get_position()}, \"{self.get_status()}\",{self.__get_item()},{self.attack},{self.defence}]"

    