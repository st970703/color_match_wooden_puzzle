import uuid

from tile import Diamond, PuzzleShape, Tile

NUM_OF_TILES_FOR_2_BY_2_DIAMOND = 4


def check_if_satisfies_2_by_2_diamond_constraints(path: list[Tile]) -> bool:
    return (
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


def solve_central_2_by_2_diamond(
    tiles: list[Tile], results: list, path: list[Tile] = []
):
    """
    Finds the central_2_by_2_diamond.
    Uses backtracking.
    Solve by filling the list of length 4
    with CW order:
    top (index 0) - right
     - bottom - left (index 3).
    """
    # Base case
    if len(path) == NUM_OF_TILES_FOR_2_BY_2_DIAMOND:
        for index_in_path in range(0, len(path)):
            for num_of_rotations in range(0, 4):
                path[index_in_path].rotate_cw_90()
                if check_if_satisfies_2_by_2_diamond_constraints(path):
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


def check_if_satisfies_diamond_left_edge_constraints(
    path: list[Tile], left_tile_of_diamond: Tile
) -> bool:
    return (
        len(path) == NUM_OF_TILES_FOR_DIAMOND_EDGE
        and left_tile_of_diamond.top == path[0].right
        and left_tile_of_diamond.left == path[0].bottom
        and left_tile_of_diamond.left == path[1].top
        and left_tile_of_diamond.bottom == path[1].right
    )


def solve_diamond_left_edge_tiles(
    tiles: list[Tile], left_tile_of_diamond: Tile, results: list, path: list[Tile] = []
):
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
    if len(path) == NUM_OF_TILES_FOR_DIAMOND_EDGE:
        for index_in_path in range(0, len(path)):
            for num_of_rotations in range(0, 4):
                path[index_in_path].rotate_cw_90()
                if check_if_satisfies_diamond_left_edge_constraints(
                    path=path, left_tile_of_diamond=left_tile_of_diamond
                ):
                    results.append(path.copy())
    # Recursive case
    for tile in tiles:
        if tile not in path:
            # Choose
            path.append(tile)

            # Explore
            solve_diamond_left_edge_tiles(
                tiles=tiles,
                left_tile_of_diamond=left_tile_of_diamond,
                results=results,
                path=path,
            )

            # Unchoose (backtrack)
            path.pop()


def check_if_satisfies_diamond_right_edge_constraints(
    path: list[Tile], right_tile_of_diamond: Tile
) -> bool:
    return (
        len(path) == NUM_OF_TILES_FOR_DIAMOND_EDGE
        and right_tile_of_diamond.top == path[0].left
        and right_tile_of_diamond.right == path[0].bottom
        and right_tile_of_diamond.right == path[1].top
        and right_tile_of_diamond.bottom == path[1].left
    )


def solve_diamond_right_edge_tiles(
    tiles: list[Tile], right_tile_of_diamond: Tile, results: list, path: list[Tile] = []
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
    if len(path) == NUM_OF_TILES_FOR_DIAMOND_EDGE:
        for index_in_path in range(0, len(path)):
            for num_of_rotations in range(0, 4):
                path[index_in_path].rotate_cw_90()
                if check_if_satisfies_diamond_right_edge_constraints(
                    path=path, right_tile_of_diamond=right_tile_of_diamond
                ):
                    results.append(path.copy())

    # Recursive case
    for tile in tiles:
        if tile not in path:
            # Choose
            path.append(tile)

            # Explore
            solve_diamond_right_edge_tiles(
                tiles=tiles,
                right_tile_of_diamond=right_tile_of_diamond,
                results=results,
                path=path,
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
        lists_of_left_edge_tiles: list[list[Tile]] = []
        index_for_diamond_left = 3
        left_tile_of_diamond = diamond[index_for_diamond_left]
        solve_diamond_left_edge_tiles(
            tiles=unused_tiles,
            left_tile_of_diamond=left_tile_of_diamond,
            results=lists_of_left_edge_tiles,
        )
        if not lists_of_left_edge_tiles:
            continue
        for left_edge_tiles in lists_of_left_edge_tiles:
            left_edge_tile_ids: set[uuid.UUID] = {tile.id for tile in left_edge_tiles}
            unused_tiles = [
                tile for tile in unused_tiles if tile.id not in left_edge_tile_ids
            ]
            lists_of_right_edge_tiles: list[list[Tile]] = []
            index_for_diamond_right = 1
            right_tile_of_diamond = diamond[index_for_diamond_right]
            solve_diamond_right_edge_tiles(
                tiles=unused_tiles,
                right_tile_of_diamond=right_tile_of_diamond,
                results=lists_of_right_edge_tiles,
            )
            if not lists_of_right_edge_tiles:
                continue
            for right_edge_tiles in lists_of_right_edge_tiles:
                puzzle_shape = PuzzleShape(
                    diamond=Diamond(
                        top=diamond[0],
                        right=diamond[1],
                        bottom=diamond[2],
                        left=diamond[3],
                    ),
                    left_edge_top=left_edge_tiles[0],
                    left_edge_bottom=left_edge_tiles[1],
                    right_edge_top=right_edge_tiles[0],
                    right_edge_bottom=right_edge_tiles[1],
                )
                results.append(puzzle_shape)
    return results
