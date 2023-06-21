class Knight:

    def __init__(self, x, y, defence, attack, colour) -> None:
        self.x = x
        self.y = y
        self.defence = defence
        self.attack = attack
        self.item = None
        self.dead = False
        self.drowned = False
        self.colour = self.set_colour(colour)


    def get_status(self):
        if self.drowned:
            return "DROWNED"
        if self.dead:
            return "DEAD"
        return "LIVE"
    
    def get_position(self):
        return [self.x,self.y]

    def set_colour(self,colour):
        if colour == "R":
            self.colour = "Red"
        if colour == "G":
            self.colour = "Green"
        if colour == "B":
            self.colour = "Blue"
        if colour == "Y":
            self.colour = "Yellow"


    def __str__(self) -> str:
        return f"{self.colour}"

    