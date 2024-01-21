# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from colours import Colour
from solve import solve_puzzle
from tile import Tile

if __name__ == "__main__":
    tile_0 = Tile(
        top=Colour.RED, left=Colour.YELLOW, right=Colour.BLUE, bottom=Colour.GREEN
    )
    tile_1 = Tile(
        top=Colour.GREEN, left=Colour.YELLOW, right=Colour.RED, bottom=Colour.BLUE
    )
    tile_2 = Tile(
        top=Colour.BLUE, left=Colour.GREEN, right=Colour.YELLOW, bottom=Colour.RED
    )
    tile_3 = Tile(
        top=Colour.GREEN, left=Colour.BLUE, right=Colour.RED, bottom=Colour.YELLOW
    )
    tile_4 = Tile(
        top=Colour.YELLOW, left=Colour.RED, right=Colour.BLUE, bottom=Colour.GREEN
    )
    tile_5 = Tile(
        top=Colour.RED, left=Colour.YELLOW, right=Colour.GREEN, bottom=Colour.BLUE
    )
    tile_6 = Tile(
        top=Colour.BLUE, left=Colour.RED, right=Colour.YELLOW, bottom=Colour.GREEN
    )
    tile_7 = Tile(
        top=Colour.GREEN, left=Colour.BLUE, right=Colour.YELLOW, bottom=Colour.RED
    )

    tiles = [
        tile_0,
        tile_1,
        tile_2,
        tile_3,
        tile_4,
        tile_5,
        tile_6,
        tile_7,
    ]

    results = solve_puzzle(tiles)
    print(str(results))
