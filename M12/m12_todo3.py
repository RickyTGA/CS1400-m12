class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    def __init__(self, corner1, corner2):
        if not isinstance(corner1, Point) or not isinstance(corner2, Point):
            raise TypeError("Rectangle corners must be Point instances")
        self.corner1 = corner1
        self.corner2 = corner2

    def midpoint(self):
        """Return the center point of the rectangle."""
        mx = (self.corner1.x + self.corner2.x) / 2.0
        my = (self.corner1.y + self.corner2.y) / 2.0
        return Point(mx, my)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(4, 6)
    r = Rectangle(p1, p2)
    print("Rectangle midpoint:", r.midpoint())  # Point(2.0, 3.0)
