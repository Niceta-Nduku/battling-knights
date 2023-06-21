class Item:

    def __init__(self, x, y, defence, attack, name) -> None:
        self.x = x
        self.y = y
        self.defence = defence
        self.attack = attack
        self.name = name
        self.equipped = False
    
    def get_position(self):
        return [self.x,self.y]
    
    def __str__(self) -> str:
        return f"\"{self.name}\" : [{self.get_position()},{self.equipped}]"
    
