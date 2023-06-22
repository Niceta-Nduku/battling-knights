


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
                    square.occupant_knights.append(piece)
                    self.knights["Red"] = piece
                    continue

                # add second knight
                # Y (0,7) (top right)
                if (x == 0) and (y == 7):
                    piece = Knight(x, y, 1, 1, "Yellow")
                    square.occupant_knights.append(piece)
                    self.knights["Yellow"] = piece
                    continue

                # add first Item
                # Axe (A) (2,2)
                # Axe (A): +2 Attack
                if (x == 2) and (y == 2):
                    piece = Item(x,y,defence=0,attack=2,name="Axe")
                    square.occupant_items.append(piece)
                    self.items["Axe"] = piece
                    continue

                # add second Item
                # Dagger (D) (2,5)
                # Dagger (D): +1 Attack
                if (x == 2) and (y == 5):
                    piece = Item(x,y,defence=0,attack=1,name="Dagger")
                    square.occupant_items.append(piece)
                    self.items["Dagger"] = piece
                    continue

                # add third Item
                # MagicStaff (M) (5,2)
                # MagicStaff (M): +1 Attack, +1 Defence
                if (x == 5) and (y == 2):
                    piece = Item(x,y,defence=1,attack=1,name="MagicStaff")
                    square.occupant_items.append(piece)
                    self.items["MagicStaff"] = piece
                    continue

                # add fourth Item
                # Helmet (H) (5,5)
                # Helmet (H): +1 Defence
                if (x == 5) and (y == 5):
                    piece = Item(x,y,defence=1,attack=0,name="Helmet")
                    square.occupant_items.append(piece)
                    self.items["Helmet"] = piece
                    continue

                # add third knight
                # B (7,0) (bottom left)
                if (x == 7) and (y == 0):
                    piece = Knight(x, y, 1, 1, "Blue")
                    square.occupant_knights.append(piece)
                    self.knights["Blue"] = piece
                    continue

                # add fourth knight
                # G (7,7) (bottom right)
                if (x == 7) and (y == 7):
                    piece = Knight(x, y, 1, 1, "Green")
                    square.occupant_knights.append(piece)
                    self.knights["Green"] = piece 
                    continue

        # get board layout
        def print_board(self):
            
            for knight in self.knights:
                print(self.knights[knight])

            for item in self.items:
                print(self.items[item])

                

    # move knight

        def move(knight, direction):
            # 0. check if dead or drowned, if not continue
            # 1. get current position
            # 2. get new position
            # 3. check if within boundaries
            # 3.2 if outside drown
            # 4. get tile in new position
            # 5. get occupied knight
            # 6.1 if knight null continue
            # 6.1.1 if there is one item and knight not equiped , equip
            # 6.1.2 if there is more item and knight not equiped, get best 
            # 6.1.3 if knight is equiped, continue
            # 6.2 if knight is not null
            # 6.2.1 fight



            if knight == "R":
                active_knight = self.knights["Red"]

            if knight == "B":
                active_knight = self.knights["Blue"]

            if knight == "G":
                active_knight = self.knights["Green"]

            if knight == "Y":
                active_knight = self.knights["Yellow"]

            if active_knight.dead or active_knight.drowned:
                return
            
            current_x = active_knight.x
            current_y = active_knight.y
            
            if direction == "N":
                new_y = current_y - 1
                new_x = current_x

            if direction == "S":
                new_y = current_y + 1
                new_x = current_x

            if direction == "E":
                new_y = current_y
                new_x = current_x + 1 
            
            if direction == "W":
                new_y = current_y
                new_x = current_x - 1

            if new_y < 0 or new_y > 7 or new_x < 0 or new_x > 7:

                active_knight.drowned = True
                return
            
            tile = get_tile_in_position(new_x,new_y)

            if len(tile.occupant_knights) > 0:
                #fight
                pass
            elif len(tile.occupant_items) > 0:
                #equip
                pass
            else:
                #move to new tile
            

            


            
        def get_tile_in_position(x,y):
            return self.tiles[8 * x + y] 

    # equip knight

    # drown

    # fight

    # result
