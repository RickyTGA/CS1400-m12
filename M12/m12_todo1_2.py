class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, p1, p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError("Line endpoints must be Point instances")
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        """Return True when the endpoints are the same points in any order."""
        if not isinstance(other, Line):
            return NotImplemented
        return ((self.p1 == other.p1 and self.p2 == other.p2)
                or (self.p1 == other.p2 and self.p2 == other.p1))

    def midpoint(self):
        """Return the midpoint of the line segment as a Point."""
        mx = (self.p1.x + self.p2.x) / 2.0
        my = (self.p1.y + self.p2.y) / 2.0
        return Point(mx, my)


if __name__ == "__main__":
    # Quick self-checks
    a = Point(0, 0)
    b = Point(2, 2)
    l1 = Line(a, b)
    l2 = Line(Point(2, 2), Point(0, 0))
    print("l1 == l2?", l1 == l2)  # True
    mid = l1.midpoint()
    print("midpoint:", mid)  # Point(1.0, 1.0)
