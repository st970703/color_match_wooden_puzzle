import pytest

from colours import Colour
<<<<<<< HEAD
from solve import solve_puzzle, solve_central_2_by_2_diamond
from tile import Tile, PuzzleShape, Diamond
=======
from solve import solve_central_2_by_2_diamond, solve_puzzle
from tile import Diamond, Tile
>>>>>>> 346a53e8fec7445e85ef6f666824f576630b367d


def assert_the_two_by_two_diamond_is_solved(diamond: Diamond):
    assert diamond.top.right == diamond.right.top
    assert diamond.top.bottom == diamond.right.left
    assert diamond.right.left == diamond.bottom.top
    assert diamond.right.bottom == diamond.bottom.right
    assert diamond.bottom.top == diamond.left.right
    assert diamond.bottom.left == diamond.left.bottom
    assert diamond.left.top == diamond.top.left
    assert diamond.left.right == diamond.top.bottom


def assert_the_left_edge_tiles_are_solved(
    left_edge_top: Tile, left_edge_bottom: Tile, diamond: Diamond
):
    assert left_edge_top.right == diamond.left.top
    assert left_edge_top.bottom == diamond.left.left
    assert left_edge_bottom.top == diamond.left.left
    assert left_edge_bottom.right == diamond.left.bottom

<<<<<<< HEAD
def assert_the_puzzle_is_solved(puzzle_shape: PuzzleShape):
    assert_the_two_by_two_diamond_is_solved(puzzle_shape.diamond)
    assert_the_left_edge_tiles_are_solved(puzzle_shape)
    assert_the_right_edge_tiles_are_solved(puzzle_shape)
=======

def assert_the_right_edge_tiles_are_solved(
    right_edge_top: Tile, right_edge_bottom: Tile, diamond: Diamond
):
    assert right_edge_top.left == diamond.right.top
    assert right_edge_top.bottom == diamond.right.right
    assert right_edge_bottom.top == diamond.right.right
    assert right_edge_bottom.left == diamond.right.bottom
>>>>>>> 346a53e8fec7445e85ef6f666824f576630b367d


class TestPuzzleSolve:
    @pytest.fixture
    def make_eight_tiles(self) -> list[Tile]:
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

        return [
            tile_0,
            tile_1,
            tile_2,
            tile_3,
            tile_4,
            tile_5,
            tile_6,
            tile_7,
        ]

    def test_puzzle_solve(self, make_eight_tiles: list[Tile]) -> None:
        results = solve_puzzle(make_eight_tiles)
        assert len(results) > 0
        for puzzle_shape in results:
            assert_the_two_by_two_diamond_is_solved(puzzle_shape.diamond)
            assert_the_left_edge_tiles_are_solved(
                left_edge_top=puzzle_shape.left_edge_top,
                left_edge_bottom=puzzle_shape.left_edge_bottom,
                diamond=puzzle_shape.diamond,
            )
            assert_the_right_edge_tiles_are_solved(
                right_edge_top=puzzle_shape.right_edge_top,
                right_edge_bottom=puzzle_shape.right_edge_bottom,
                diamond=puzzle_shape.diamond,
            )

    def test_tile_rotation(self):
        tile = Tile(
            top=Colour.RED, left=Colour.YELLOW, right=Colour.BLUE, bottom=Colour.GREEN
        )
        tile.rotate_cw_90()

        assert tile.top == Colour.YELLOW
        assert tile.right == Colour.RED
        assert tile.bottom == Colour.BLUE
        assert tile.left == Colour.GREEN

<<<<<<< HEAD

    def test_solve_central_2_by_2_diamond(
        self,
        make_eight_tiles: list[Tile]
    ):
        two_by_two_diamonds: list[list[Tile]] = []
        solve_central_2_by_2_diamond(
            tiles=make_eight_tiles,
            results=two_by_two_diamonds
=======
    def test_solve_central_2_by_2_diamond(self, make_eight_tiles: list[Tile]):
        two_by_two_diamonds: list[list[Tile]] = []
        solve_central_2_by_2_diamond(
            tiles=make_eight_tiles, results=two_by_two_diamonds
>>>>>>> 346a53e8fec7445e85ef6f666824f576630b367d
        )

        assert len(two_by_two_diamonds) > 0

        for tiles in two_by_two_diamonds:
<<<<<<< HEAD
            diamond = Diamond(top=tiles[0], right=tiles[1], bottom=tiles[2], left=tiles[3])
=======
            diamond = Diamond(
                top=tiles[0], right=tiles[1], bottom=tiles[2], left=tiles[3]
            )
>>>>>>> 346a53e8fec7445e85ef6f666824f576630b367d
            assert_the_two_by_two_diamond_is_solved(diamond)
