import pytest

from colours import Colour
from solve import solve_puzzle
from tile import Tile, PuzzleShape


def assert_the_two_by_two_diamond_is_solved(puzzle_shape: PuzzleShape):
    assert puzzle_shape.diamond.top.right == puzzle_shape.diamond.right.top
    assert puzzle_shape.diamond.top.bottom == puzzle_shape.diamond.right.left
    assert puzzle_shape.diamond.right.left == puzzle_shape.diamond.bottom.top
    assert puzzle_shape.diamond.right.bottom == puzzle_shape.diamond.bottom.right
    assert puzzle_shape.diamond.bottom.top == puzzle_shape.diamond.left.right
    assert puzzle_shape.diamond.bottom.left == puzzle_shape.diamond.left.bottom
    assert puzzle_shape.diamond.left.top == puzzle_shape.diamond.top.left
    assert puzzle_shape.diamond.left.right == puzzle_shape.diamond.top.bottom

def assert_the_left_edge_tiles_are_solved(puzzle_shape: PuzzleShape):
    assert puzzle_shape.left_edge_top.right == puzzle_shape.diamond.left.top
    assert puzzle_shape.left_edge_top.bottom == puzzle_shape.diamond.left.left
    assert puzzle_shape.left_edge_bottom.top == puzzle_shape.diamond.left.left
    assert puzzle_shape.left_edge_bottom.right == puzzle_shape.diamond.left.bottom

def assert_the_right_edge_tiles_are_solved(puzzle_shape: PuzzleShape):
    assert puzzle_shape.right_edge_top.left == puzzle_shape.diamond.right.top
    assert puzzle_shape.right_edge_top.bottom == puzzle_shape.diamond.right.right
    assert puzzle_shape.right_edge_bottom.top == puzzle_shape.diamond.right.right
    assert puzzle_shape.right_edge_bottom.left == puzzle_shape.diamond.right.bottom

def assert_the_puzzle_is_solved(puzzle_shape: PuzzleShape):
    assert_the_two_by_two_diamond_is_solved(puzzle_shape)
    assert_the_left_edge_tiles_are_solved(puzzle_shape)
    assert_the_right_edge_tiles_are_solved(puzzle_shape)


class TestPuzzleSolve:
    @pytest.fixture
    def make_eight_tiles(self) -> list[Tile]:
        tile_0 = Tile(top=Colour.RED, left=Colour.YELLOW, right=Colour.BLUE, bottom=Colour.GREEN)
        tile_1 = Tile(top=Colour.GREEN, left=Colour.YELLOW, right=Colour.RED, bottom=Colour.BLUE)
        tile_2 = Tile(top=Colour.BLUE, left=Colour.GREEN, right=Colour.YELLOW, bottom=Colour.RED)
        tile_3 = Tile(top=Colour.GREEN, left=Colour.BLUE, right=Colour.RED, bottom=Colour.YELLOW)
        tile_4 = Tile(top=Colour.YELLOW, left=Colour.RED, right=Colour.BLUE, bottom=Colour.GREEN)
        tile_5 = Tile(top=Colour.RED, left=Colour.YELLOW, right=Colour.GREEN, bottom=Colour.BLUE)
        tile_6 = Tile(top=Colour.BLUE, left=Colour.RED, right=Colour.YELLOW, bottom=Colour.GREEN)
        tile_7 = Tile(top=Colour.GREEN, left=Colour.BLUE, right=Colour.YELLOW, bottom=Colour.RED)

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

    def test_puzzle_solve(
        self,
        make_eight_tiles: list[Tile]
    ) -> None:
        results = solve_puzzle(make_eight_tiles)

        for result in results:
            assert_the_puzzle_is_solved(result)
