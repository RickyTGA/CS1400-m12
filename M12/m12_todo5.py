class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Circle:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise TypeError("center must be a Point")
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def draw(self):
        """Attempt to draw using jupyturtle; fall back to the standard turtle module.

        This method assumes a typical turtle-like API (penup, goto, pendown, circle).
        """
        try:
            import jupyturtle as jt
            turtle_lib = jt
        except Exception:
            try:
                import turtle as turtle_lib
            except Exception:
                raise RuntimeError("No turtle-like drawing library available (jupyturtle/turtle)")

        # Draw circle centered at (center.x, center.y). turtle.circle draws relative to current position,
        # so move to (center.x, center.y - radius) then draw.
        turtle_lib.penup()
        turtle_lib.goto(self.center.x, self.center.y - self.radius)
        turtle_lib.setheading(0)
        turtle_lib.pendown()
        turtle_lib.circle(self.radius)
        turtle_lib.penup()


if __name__ == "__main__":
    c = Circle(Point(0, 0), 50)
    print(c)
    # To actually draw, run this module interactively; drawing may open a window.
