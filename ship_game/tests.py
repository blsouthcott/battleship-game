
import unittest

from ship_game.ShipGame import ShipGame


class ShipGameTester(unittest.TestCase):

    def test_game_1(self):
        sg = ShipGame()
        self.assertTrue(sg.place_ship("first", 4, "G9", "C"))
        self.assertTrue(sg.place_ship("second", 3, "E3", "R"))

        self.assertTrue(sg.place_ship("first", 5, "D2", "R"))
        self.assertTrue(sg.place_ship("second", 6, "B10", "C"))

        self.assertFalse(sg.place_ship("first", 3, "H7", "R"))
        self.assertFalse(sg.place_ship("second", 3, "E8", "R"))

        self.assertTrue(sg.fire_torpedo("first", "B10"))
        self.assertTrue(sg.fire_torpedo("second", "G9"))

        self.assertTrue(sg.fire_torpedo("first", "E3"))
        self.assertTrue(sg.fire_torpedo("second", "H9"))

        self.assertTrue(sg.fire_torpedo("first", "E4"))
        self.assertTrue(sg.fire_torpedo("second", "I9"))

        self.assertTrue(sg.fire_torpedo("first", "E5"))
        self.assertEqual(sg.get_num_ships_remaining("second"), 1)
        self.assertTrue(sg.fire_torpedo("second", "J9"))
        self.assertEqual(sg.get_num_ships_remaining("first"), 1)

        self.assertTrue(sg.fire_torpedo("first", "C10"))
        self.assertTrue(sg.fire_torpedo("second", "D2"))

        self.assertTrue(sg.fire_torpedo("first", "D10"))
        self.assertTrue(sg.fire_torpedo("second", "D3"))

        self.assertTrue(sg.fire_torpedo("first", "E10"))
        self.assertTrue(sg.fire_torpedo("second", "D4"))

        self.assertTrue(sg.fire_torpedo("first", "F10"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "G10"))
        self.assertEqual(sg.get_current_state(), "FIRST_WON")
        self.assertFalse(sg.fire_torpedo("second", "D6"))

    def test_game_2(self):
        sg = ShipGame()

        # place ships
        sg.place_ship("first", 3, "A1", "R")
        sg.place_ship("second", 4, "B1", "R")
        sg.place_ship("first", 3, "C1", "R")
        sg.place_ship("second", 4, "D1", "R")

        self.assertFalse(sg.place_ship("first", 5, "A1", "C"))
        self.assertFalse(sg.place_ship("first", 12, "A1", "C"))
        self.assertFalse(sg.place_ship("second", 7, "B9", "R"))

        sg.place_ship("first", 4, "G9", "C")
        sg.place_ship("second", 4, "G9", "C")

        self.assertFalse(sg.place_ship("first", 3, "H8", "R"))
        self.assertFalse(sg.place_ship("second", 3, "J8", "R"))

        sg.place_ship("first", 8, "A10", "C")
        sg.place_ship("second", 6, "E1", "C")

        # fire torpedoes
        self.assertTrue(sg.fire_torpedo("first", "B1"))
        self.assertTrue(sg.fire_torpedo("second", "D2"))

        self.assertTrue(sg.fire_torpedo("first", "B2"))
        self.assertTrue(sg.fire_torpedo("second", "D3"))

        self.assertTrue(sg.fire_torpedo("first", "B3"))
        self.assertTrue(sg.fire_torpedo("second", "D4"))

        self.assertTrue(sg.fire_torpedo("first", "B4"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertEqual(sg.get_num_ships_remaining("first"), 4)
        self.assertEqual(sg.get_num_ships_remaining("second"), 3)

        self.assertTrue(sg.fire_torpedo("first", "D1"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "D2"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "D3"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "D4"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertEqual(sg.get_num_ships_remaining("first"), 4)
        self.assertEqual(sg.get_num_ships_remaining("second"), 2)

        self.assertTrue(sg.fire_torpedo("first", "G9"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "H9"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "I9"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "J9"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertEqual(sg.get_num_ships_remaining("first"), 4)
        self.assertEqual(sg.get_num_ships_remaining("second"), 1)

        self.assertTrue(sg.fire_torpedo("first", "E1"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "F1"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "G1"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "H1"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "I1"))
        self.assertTrue(sg.fire_torpedo("second", "D5"))

        self.assertTrue(sg.fire_torpedo("first", "J1"))
        self.assertEqual(sg.get_num_ships_remaining("second"), 0)
        self.assertEqual(sg._current_players_turn, "second")
        self.assertFalse(sg.fire_torpedo("second", "D5"))


if __name__ == "__main__":
    unittest.main()
