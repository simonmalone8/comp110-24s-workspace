"""CQ08."""

from __future__ import annotations
 
__author__ = "730476889"


class Point:
    """Creates a Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Scales the point in-place by factor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Returns a new Point scaled by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scales the point and returns a new Point object."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point