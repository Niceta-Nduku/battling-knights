from game.tile import Tile
from game.knight import Knight
from game.item import Item
import json


class Game:

    def __init__(self) -> None:
        self.tiles = []
        self.knights = {"red": None, "blue": None,
                        "green": None, "yellow": None}
        self.items = {"magic_staff": None,
                      "helmet": None, "dagger": None, "axe": None}

        self.set_up()

    # set up game
    # - Create Tiles -> knights - > items

    def set_up(self):

        for x in range(8):
            for y in range(8):
                square = Tile(x, y)
                self.tiles.append(square)

                # add first knight
                # R (0,0) (top left)
                if (x == 0) and (y == 0):
                    piece = Knight(x, y, 1, 1, "red")
                    square.occupant_knight = piece
                    self.knights["red"] = piece
                    continue

                # add second knight
                # Y (0,7) (top right)
                if (x == 0) and (y == 7):
                    piece = Knight(x, y, 1, 1, "yellow")
                    square.occupant_knight = piece
                    self.knights["yellow"] = piece
                    continue

                # add first Item
                # axe (A) (2,2)
                # axe (A): +2 Attack
                if (x == 2) and (y == 2):
                    piece = Item(x, y, defence=0, attack=2, name="axe")
                    square.occupant_items.append(piece)
                    self.items["axe"] = piece
                    continue

                # add second Item
                # dagger (D) (2,5)
                # dagger (D): +1 Attack
                if (x == 2) and (y == 5):
                    piece = Item(x, y, defence=0, attack=1, name="dagger")
                    square.occupant_items.append(piece)
                    self.items["dagger"] = piece
                    continue

                # add third Item
                # magic_staff (M) (5,2)
                # magic_staff (M): +1 Attack, +1 Defence
                if (x == 5) and (y == 2):
                    piece = Item(x, y, defence=1, attack=1, name="magic_staff")
                    square.occupant_items.append(piece)
                    self.items["magic_staff"] = piece
                    continue

                # add fourth Item
                # helmet (H) (5,5)
                # helmet (H): +1 Defence
                if (x == 5) and (y == 5):
                    piece = Item(x, y, defence=1, attack=0, name="helmet")
                    square.occupant_items.append(piece)
                    self.items["helmet"] = piece
                    continue

                # add third knight
                # B (7,0) (bottom left)
                if (x == 7) and (y == 0):
                    piece = Knight(x, y, 1, 1, "blue")
                    square.occupant_knight = piece
                    self.knights["blue"] = piece
                    continue

                # add fourth knight
                # G (7,7) (bottom right)
                if (x == 7) and (y == 7):
                    piece = Knight(x, y, 1, 1, "green")
                    square.occupant_knight = piece
                    self.knights["green"] = piece
                    continue

    # get board layout

    def print_board(self):

        results = {"red": None, "blue": None,
                   "green": None, "yellow": None, "magic_staff": None,
                   "helmet": None, "dagger": None, "axe": None}

        for knight in self.knights:
            print(self.knights[knight])
            results[knight] = self.knights[knight].get_attributes()

        for item in self.items:
            print(self.items[item])
            results[item] = self.items[item].get_attributes()

            # Serializing json
        json_object = json.dumps(results, indent=1)

        # Writing to sample.json
        with open("results.json", "w") as outfile:
            outfile.write(json_object)

    # move knight

    def move(self, knight, direction):
        # 0. check if dead or drowned, if not continue
        # 1. get current position
        # 2. get new position
        # 3. check if within boundaries
        # 3.2 if outside drownpass
        # 4. get tile in new position
        # 5. get occupied knight or item
        # 6.1 if item
        # 6.1.1 if there is one item and knight not equiped , equip
        # 6.1.2 if there is more item and knight not equiped, get best
        # 6.1.3 if knight is equiped, continue
        # 6.2 if knight is not null
        # 6.2.1 fight

        if knight == 'R':
            active_knight = self.knights["red"]

        elif knight == 'B':
            active_knight = self.knights["blue"]

        elif knight == 'G':
            active_knight = self.knights["green"]

        elif knight == 'Y':
            active_knight = self.knights["yellow"]
        else:
            raise Exception('Invalid knight. Please give a valid knight')

        if active_knight.dead or active_knight.drowned:
            return

        current_x = active_knight.x
        current_y = active_knight.y

        if direction == 'N':
            new_y = current_y
            new_x = current_x - 1

        elif direction == 'S':
            new_y = current_y
            new_x = current_x + 1

        elif direction == 'E':
            new_y = current_y + 1
            new_x = current_x

        elif direction == 'W':
            new_y = current_y - 1
            new_x = current_x
        else:
            raise Exception(
                'Invalid direction. Please Enter a valid direction')

        if new_y < 0 or new_y > 7 or new_x < 0 or new_x > 7:
            self.__drown(active_knight)
            return

        # update tile position
        active_knight.x = new_x
        active_knight.y = new_y

        tile = self.__get_tile_in_position(self.tiles, new_x, new_y)

        if active_knight.item == None:
            if len(tile.occupant_items) > 0:
                self.__equip_knight(tile.occupant_items, active_knight)
                tile.occupant_items.remove(active_knight.item)

        else:
            # move with item
            active_knight.item.x = new_x
            active_knight.item.y = new_y

        if tile.occupant_knight == None:
            # new tile occupant
            tile.occupant_knight = active_knight

        else:
            if (self.__fight(active_knight, tile.occupant_knight)):
                # if won the fight, new occupant
                tile.occupant_knight = active_knight

    def __get_tile_in_position(self, tiles, x, y):
        pos = 8 * x + y
        if pos > 0 or pos < 64:
            return tiles[pos]

    # equip knight
    def __equip_knight(self, items, knight):
        # loop through array
        # check if item is equiped
        # equip and add attack or defence

        for item in items:
            if item.equipped:
                continue

            if (item.name == "axe"):
                self.__equip(knight, item)
                break

            elif (item.name == "magic_staff"):
                self.__equip(knight, item)
                break

            elif (item.name == "dagger"):
                self.__equip(knight, item)
                break

            elif (item.name == "helmet"):
                self.__equip(knight, item)
                break

    # equip
    def __equip(self, knight, item):
        knight.item = item
        item.equpied = True
        knight.attack = item.attack
        knight.defence = item.defence

    # fight
    def __fight(self, knight_one, knight_two):
        # knight one is attacker

        # add 0.5 and item modifiers
        knight_one.attack = knight_one.attack + 0.5

        # compare results
        if knight_one.attack > knight_two.defence:
            # knight two dies
            self.__die(knight_two)
            return True

        else:
            # knight one dies
            self.__die(knight_one)
            return False

    def __drown(self, knight):
        # change position to None
        # change attack or defence to 0
        knight.drowned = True
        knight.x = None
        knight.y = None
        knight.defence = 0
        knight.attack = 0
        knight.item = None

    def __die(self, knight):
        knight.dead = True
        knight.defence = 0
        knight.attack = 0
        knight.item = None
