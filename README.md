# battleship-game
ShipGame.py contains ShipGame class which provides an interface for playing Battleship. 

Also contains Ship and Player classes, which are used in ShipGame class. Ship class holds the coordinates for
the ship and Player class holds the ships for the player. Player class also holds a set of all coordinates
occupied by ships for that player at the time all ships have been placed, which is used to validate each
new ship placement.

## To use this
Download the zip file, extract, and in your local directory run

`pip install --user .`

Then import the ShipGame class like this

`from ship_game import ShipGame`

The game can then be instantiated, ships placed, and torpedoes fired as below:

```
sg = ShipGame()
sg.place_ship("first", 4, "G9", "C"))
sg.place_ship("second", 3, "E3", "R"))
sg.fire_torpedo("first", "E3") # direct hit!
sg.fire_torpedo("second", "G10") # another hit!
```
