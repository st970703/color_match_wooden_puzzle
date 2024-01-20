import uuid

from tile import Tile, PuzzleShape, Diamond

NUM_OF_TILES_FOR_2_BY_2_DIAMOND = 4
def solve_central_2_by_2_diamond(tiles: list[Tile], results: list, path: list[Tile] = []):
    """
    Finds the central_2_by_2_diamond.
    Uses backtracking.
    Solve by filling the list of length 4
    with CW order:
    top (index 0) - right
     - bottom - left (index 3).
    """
    # Base case
    satisfies_2_by_2_diamond_constraints = (
        len(path) == NUM_OF_TILES_FOR_2_BY_2_DIAMOND
        and path[0].bottom == path[1].left
        and path[0].right == path[1].top
        and path[1].left == path[2].top
        and path[1].bottom == path[2].right
        and path[2].top == path[3].right
        and path[2].left == path[3].bottom
        and path[3].top == path[0].left
        and path[3].right == path[0].bottom
    )
    if satisfies_2_by_2_diamond_constraints:
        results.append(path.copy())

    # Recursive case
    for tile in tiles:
        if tile not in path:
            # Choose
            path.append(tile)

            # Explore
            solve_central_2_by_2_diamond(tiles=tiles, results=results, path=path)

            # Unchoose (backtrack)
            path.pop()

NUM_OF_TILES_FOR_DIAMOND_EDGE = 2
def solve_diamond_left_edge_tiles(
    tiles: list[Tile],
    two_by_two_diamond: list[Tile],
    results: list,
    path: list[Tile] = []
) -> list[Tile] | None:
    """
    Solve the two edge tiles for
    the 2 by 2 diamond's left
    edge.
    The left edge should have two
    protruding tiles.
    The results list is filled top to bottom.
    <top edge tile>
                        <diamond's left tile>
    <bottom edge tile>
    :param tiles: unused tiles that are not in the two by two diamond.
    :return:
    """
    # Base case
    left_tile_of_diamond = two_by_two_diamond[3]
    satisfies_diamond_edge_constraints = (
        len(path) == NUM_OF_TILES_FOR_DIAMOND_EDGE
        and left_tile_of_diamond.top == path[0].right
        and left_tile_of_diamond.left == path[0].bottom
        and left_tile_of_diamond.left == path[1].top
        and left_tile_of_diamond.bottom == path[1].right
    )
    if satisfies_diamond_edge_constraints:
        for tile in path:
            results.append(tile)
        return

    # Recursive case
    for tile in tiles:
        if tile not in path:
            # Choose
            path.append(tile)

            # Explore
            solve_diamond_left_edge_tiles(
                tiles=tiles,
                two_by_two_diamond=two_by_two_diamond,
                results=results,
                path=path
            )

            # Unchoose (backtrack)
            path.pop()



def solve_diamond_right_edge_tiles(
    tiles: list[Tile],
    two_by_two_diamond: list[Tile],
    results: list,
    path: list[Tile] = []
):
    """
    Solve the two edge tiles for
    the 2 by 2 diamond's right
    edge.
    The right edge should have two
    protruding tiles.
    The results list is filled top to bottom.
                            <top edge tile>
    <diamond's right tile>
                            <bottom edge tile>
    :param tiles: unused tiles that are not in the two by two diamond.
    :return:
    """
    # Base case
    right_tile_of_diamond = two_by_two_diamond[1]
    satisfies_diamond_edge_constraints = (
        len(path) == NUM_OF_TILES_FOR_DIAMOND_EDGE
        and right_tile_of_diamond.top == path[0].left
        and right_tile_of_diamond.right == path[0].bottom
        and right_tile_of_diamond.right == path[1].top
        and right_tile_of_diamond.bottom == path[1].left
    )
    if satisfies_diamond_edge_constraints:
        for tile in path:
            results.append(tile)
        return

    # Recursive case
    for tile in tiles:
        if tile not in path:
            # Choose
            path.append(tile)

            # Explore
            solve_diamond_right_edge_tiles(
                tiles=tiles,
                two_by_two_diamond=two_by_two_diamond,
                results=results,
                path=path
            )

            # Unchoose (backtrack)
            path.pop()

def solve_puzzle(tiles: list[Tile]) -> list[PuzzleShape]:
    assert len(tiles) == 8

    results = []

    # Find the central 2 by 2 diamonds first.
    two_by_two_diamonds: list[list[Tile]] = []
    solve_central_2_by_2_diamond(tiles=tiles, results=two_by_two_diamonds)
    for diamond in two_by_two_diamonds:
        used_tile_ids: set[uuid.UUID] = {tile.id for tile in diamond}
        unused_tiles = [tile for tile in tiles if tile.id not in used_tile_ids]
        left_edge_tiles: list[Tile] = []
        solve_diamond_left_edge_tiles(
            tiles=unused_tiles,
            two_by_two_diamond=diamond,
            results=left_edge_tiles,
        )
        if len(left_edge_tiles) != NUM_OF_TILES_FOR_DIAMOND_EDGE:
            continue
        left_edge_tile_ids: set[uuid.UUID] = {tile.id for tile in left_edge_tiles}
        unused_tiles = [tile for tile in unused_tiles if tile.id not in left_edge_tile_ids]
        right_edge_tiles: list[Tile] = []
        solve_diamond_right_edge_tiles(
            tiles=unused_tiles,
            two_by_two_diamond=diamond,
            results=right_edge_tiles,
        )
        if len(right_edge_tiles) != NUM_OF_TILES_FOR_DIAMOND_EDGE:
            continue
        diamond = Diamond(
            top=diamond[0],
            right=diamond[1],
            bottom=diamond[2],
            left=diamond[3],
        )
        puzzle_shape = PuzzleShape(
            diamond=diamond,
            left_edge_top=left_edge_tiles[0],
            left_edge_bottom=left_edge_tiles[1],
            right_edge_top=right_edge_tiles[0],
            right_edge_bottom=right_edge_tiles[1],
        )
        results.append(puzzle_shape)
    return results
