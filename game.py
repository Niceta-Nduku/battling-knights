


from tile import Tile
from knight import Knight
from item import Item


class Game:

    def __init__(self) -> None:
        self.tiles = []
        self.knights = {"Red": None, "Blue": None,
                        "Green": None, "Yellow": None}
        self.items = {"Axe": None, "Dagger": None,
                        "Helmet": None, "MagicStaff": None}
        self.set_up()

    # set up game
    # - Create Tiles -> knights - > items
    def set_up(self):

        for x in range(8):
            for y in range(8):
                square = Tile(x, y)

                # add first knight
                # R (0,0) (top left)
                if (x == 0) and (y == 0):
                    piece = Knight(x, y, 1, 1, "Red")
                    square.occupant_knight = piece
                    self.knights["Red": piece]
                    continue

                # add second knight
                # Y (0,7) (top right)
                if (x == 0) and (y == 7):
                    piece = Knight(x, y, 1, 1, "Yellow")
                    square.occupant_knight = piece
                    self.knights["Yellow": piece]
                    continue

                # add first Item
                # Axe (A) (2,2)
                # Axe (A): +2 Attack
                if (x == 2) and (y == 2):
                    piece = Item(x,y,defence=0,attack=2,name="Axe")
                    square.occupant_item = piece
                    self.items["Axe": piece]
                    continue

                # add second Item
                # Dagger (D) (2,5)
                # Dagger (D): +1 Attack
                if (x == 2) and (y == 5):
                    piece = Item(x,y,defence=0,attack=1,name="Dagger")
                    square.occupant_item = piece
                    self.items["Dagger": piece]
                    continue

                # add third Item
                # MagicStaff (M) (5,2)
                # MagicStaff (M): +1 Attack, +1 Defence
                if (x == 5) and (y == 5):
                    piece = Item(x,y,defence=1,attack=1,name="MagicStaff")
                    square.occupant_item = piece
                    self.items["MagicStaff": piece]
                    continue

                # add fourth Item
                # Helmet (H) (5,5)
                # Helmet (H): +1 Defence
                if (x == 0) and (y == 0):
                    piece = Item(x,y,defence=1,attack=0,name="Helmet")
                    square.occupant_item = piece
                    self.items["Helmet": piece]
                    continue

                # add third knight
                # B (7,0) (bottom left)
                if (x == 7) and (y == 0):
                    piece = Knight(x, y, 1, 1, "Blue")
                    square.occupant_knight = piece
                    self.knights["Blue": piece]
                    continue

                # add fourth knight
                # G (7,7) (bottom right)
                if (x == 7) and (y == 7):
                    piece = Knight(x, y, 1, 1, "Green")
                    square.occupant_knight = piece
                    self.knights["Green": piece]
                    continue

                

# move knight

# equip knight

# fight

# result
