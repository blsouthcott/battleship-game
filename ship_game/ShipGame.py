

class Ship:
    """ Ship class holds the coordinates for where the ship is on the player's board.
        Coordinates are removed using the update_coordinates_per_torpedo_hit method.
        The Player class holds instances of the Ship class for each ship which is placed on the board by a player.
    """
    def __init__(self, coordinates):
        """ initialization method for Ship class
            coordinate should be a set of all coordinates the ship will occupy
        """
        self._coordinates = coordinates

    def get_coordinates(self):
        """ returns the ship's coordinates, if no coordinates have been set, returns None """
        return self._coordinates

    def update_coordinates_per_torpedo_hit(self, coordinate):
        """ coordinate should be a string indicating the coordinate to be removed from the ship's coordinates attribute
            This method should be called after the opposing player makes a move and after checking if the coordinate
            is in the ship's current coordinates.
            This method removes the coordinate from the ship's coordinates attribute.
        """
        self._coordinates.remove(coordinate)


class Player:
    """ Player class holds the player's ships. An instance of this class is initialized for each player in the ShipGame
        class.
        For use during the placement phase, the Player class also holds all coordinates occupied by the player's
        ships so far. This attribute is not updated during the torpedo firing phase of the game.
    """

    def __init__(self):
        """ initialization method for Player class takes no parameters """
        self._ships = []
        self._occupied_coordinates = set()

    def get_ships(self):
        """ returns a list containing the player's ships """
        return self._ships

    def add_ship(self, ship):
        """ adds a ship to the private list of player's ships and updates the occupied_coordinates attribute
            no return value
        """
        self._ships.append(ship)
        self._occupied_coordinates = self._occupied_coordinates.union(ship.get_coordinates())

    def remove_ship(self, ship):
        """ ships should be a Ship object, loops over the list of player's ships and removes the once that matches
            no return value
        """
        cnt = 0
        while cnt < len(self._ships):
            if ship is self._ships[cnt]:
                self._ships.pop(cnt)
            cnt += 1

    def get_occupied_coordinates(self):
        """ returns coordinates currently occupied by the player's ships """
        return self._occupied_coordinates


class ShipGame:
    """ ShipGame class provides interface for implementation of the game Battleship.
        Instances of the Player class are initialized for each player and hold instances of the Ship class for each
        ship which is placed on that player's board.
        The place_ship method should be used in the ship placing phase of the game, turns are not enforced.
        The fire_torpedo method should be used after player's have placed their ships. This method checks if the
        torpedo hit one of the opposing player's ships, and if so the update_coordinates_per_torpedo_hit method of the
        Ship class is called.
        The fire_torpedo method also updates the current player's turn and the current state of the game.
    """

    def __init__(self):
        """ initialization method takes no parameters
            sets private attributes to initial values
        """
        self._current_state = "UNFINISHED"
        self._current_players_turn = "first"
        self._first_player = Player()
        self._second_player = Player()

    def get_current_state(self):
        """ returns the current state of the game """
        return self._current_state

    def get_num_ships_remaining(self, player):
        """ player should be a string indicating first or second player
            returns the number of ships remaining for that player
        """
        if player == "first":
            player = self._first_player
        else:
            player = self._second_player

        return len(player.get_ships())

    def place_ship(self, player, ship_length, starting_ship_coordinate, ship_orientation):
        """ player should be a string indicating first or second, ship_length should be an int
            starting_ship_coordinates should be a string and ship_orientation should be a string: either R or C

            This method returns False if player does not match the current player's turn or if the ship is too small or
            would not fit on the player's board. Also returns False if the ship would overlap with a previously placed
            ship.

            Otherwise the ship's coordinates are calculated based on the ship's orientation and length and set in a
            new Ship object, and that ship is stored in the player object
        """

        if player == "first":
            player = self._first_player
        else:
            player = self._second_player

        if ship_length < 2:
            return False

        # capital A unicode integer is 65, B is 66, etc, so subtract 64 to get the row number
        row = ord(starting_ship_coordinate[0]) - 64
        # using : handles for A10, B10, C10 etc
        column = int(starting_ship_coordinate[1:])

        # adding (the ship's length - 1) to the starting coordinate tells us if the ship will fit on the board
        if ship_orientation == "R":
            if column + (ship_length - 1) > 10:
                return False
        elif ship_orientation == "C":
            if row + (ship_length - 1) > 10:
                return False

        ship_coordinates = set()
        ship_coordinates.add(starting_ship_coordinate)

        """ calculate the coordinates the ship will occupy by adding 1 to the row or column number based on the
            ship's orientation. As long as none of the coordinates are already in the occupied_coordinates attribute
            of the player class, the ship's placement is valid
        """
        for cnt in range(ship_length-1):
            if ship_orientation == "R":
                column += 1
            elif ship_orientation == "C":
                row += 1
            # add 64 to get the integer corresponding to the unicode character of the row
            next_coordinate = chr(row + 64) + str(column)
            if next_coordinate in player.get_occupied_coordinates():
                return False
            else:
                ship_coordinates.add(next_coordinate)

        ship = Ship(ship_coordinates)
        player.add_ship(ship)

        return True

    def fire_torpedo(self, player, coordinates):
        """ player should be a string indicating first or second player
            coordinates should be a string indicating where the torpedo will be fired
            returns False if player does not match the correct player's turn or game if already finished,
            otherwise returns True
        """
        if player != self._current_players_turn or self._current_state != "UNFINISHED":
            return False

        # use next player to update the current player's turn at the end of the function
        if player == "first":
            defending_player = self._second_player
            next_player = "second"
        else:
            defending_player = self._first_player
            next_player = "first"

        player_ships = defending_player.get_ships()

        for ship in player_ships:
            ship_coordinates = ship.get_coordinates()
            """ Check if the coordinates passed to the function are in any of the ship object currently on the opposing
                player's board. If so, remove them using the update_coordinates_per_torpedo_hit method
            """
            if coordinates in ship_coordinates:
                ship.update_coordinates_per_torpedo_hit(coordinates)
                if len(ship.get_coordinates()) == 0:
                    defending_player.remove_ship(ship)
                    """ Each time a ship is removed, check if it was the final ship on that player's board. If it was,
                        update the state of the game to indicate which player won.
                    """
                    if self.get_num_ships_remaining(next_player) == 0:
                        if player == "first":
                            self._current_state = "FIRST_WON"
                        else:
                            self._current_state = "SECOND_WON"

        self._current_players_turn = next_player
        return True
