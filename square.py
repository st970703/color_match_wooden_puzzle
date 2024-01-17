from dataclasses import dataclass
from colours import Colour
from enum import Enum, auto


class Side(Enum):
    TOP_LEFT = auto()
    TOP_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_RIGHT = auto()


@dataclass
class DotsToSideMapping:
    """
    ______________
    \ dot    dot \
    """
    left_dot: Colour
    right_dot: Colour
    side: Side


@dataclass
class Cube:
    top_left_: DotsToSideMapping
    top_right: DotsToSideMapping
    bottom_left: DotsToSideMapping
    bottom_right: DotsToSideMapping
