import unittest
from game.game import Game

class TestGame(unittest.TestCase):



    # board created
    # def test_set_up(self):
    #     new_game = Game()
    #     self.assertEqual(len(new_game.knights), 4, 'Knights less')
    #     self.assertEqual(len(new_game.items), 4, 'Item less')
    #     self.assertEqual(len(new_game.knights), 4, 'Knights less')
    #     self.assertEqual(len(new_game.knights), 4, 'Knights less')

    # move one knight
    def test_move(self):
        new_game = Game()
        new_game.move("R","S")

        self.assertEqual(new_game.knights["red"].x, 1)

    # equip knight

    def test_equip(self):
        new_game = Game()
        new_game.move("Y","S")
        new_game.move("Y","S")
        new_game.move("Y","W")
        new_game.move("Y","W")

        self.assertEqual(new_game.knights["yellow"].item.name, "dagger", 'wrong item collected')

    # drown knight
    def test_drown(self):
        new_game = Game()
        new_game.move("B","S")

        self.assertEqual(new_game.knights["blue"].x, None)

    # fight
    def test_fight(self):
        new_game = Game()
        new_game.move("R","S")
        new_game.move("R","S")
        new_game.move("R","E")
        new_game.move("R","E")
        new_game.move("B","N")
        new_game.move("B","N")
        new_game.move("B","E")
        new_game.move("B","E")
        new_game.move("B","N")
        new_game.move("B","N")
        new_game.move("B","N")

        self.assertEqual(new_game.knights["red"].dead, True)


    # attempt move after dead 
    def test_move_after_death(self):
        new_game = Game()
        new_game.move("R","S")
        new_game.move("R","S")
        new_game.move("R","E")
        new_game.move("R","E")
        new_game.move("B","N")
        new_game.move("B","N")
        new_game.move("B","E")
        new_game.move("B","E")
        new_game.move("B","N")
        new_game.move("B","N")
        new_game.move("B","N")
        new_game.move("R","W")

        self.assertEqual(new_game.knights["red"].y, 2)

    # attempt move after drown (with weapon)
    def test_move_after_drowm(self):
        new_game = Game()
        new_game.move("B","N")
        new_game.move("B","N")
        new_game.move("B","E")
        new_game.move("B","E")
        new_game.move("B","S")
        new_game.move("B","S")
        new_game.move("B","S")
        

        self.assertEqual(new_game.items["magic_staff"].x, 7)


if __name__ == '__main__':
    unittest.main()
