class Tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.occupant_items = []
        self.occupant_knight = None