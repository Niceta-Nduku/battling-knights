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
        return [self.x,self.y]


    def __str__(self) -> str:
        return f"{self.colour}"

    