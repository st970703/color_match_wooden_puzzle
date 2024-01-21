import uuid
from dataclasses import dataclass, field

from colours import Colour


@dataclass
class Tile:
    # Visualise this as a square rotated 45 degrees
    top: Colour
    bottom: Colour
    left: Colour
    right: Colour
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def rotate_cw_90(self):
        existing_right = self.right
        self.right = self.top
        existing_bottom = self.bottom
        self.bottom = existing_right
        existing_left = self.left
        self.left = existing_bottom
        self.top = existing_left


@dataclass
class Diamond:
    # Visualise this as a square rotated 45 degrees
    top: Tile
    bottom: Tile
    left: Tile
    right: Tile

@dataclass
class PuzzleShape:
    diamond: Diamond
    left_edge_top: Tile
    left_edge_bottom: Tile
    right_edge_top: Tile
    right_edge_bottom: Tile
