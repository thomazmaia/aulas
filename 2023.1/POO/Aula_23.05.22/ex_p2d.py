class P3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


class P2D(P3D):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, 0)

    def __add__(self, p):
        return P2D(self.x + p.x, self.y + p.y)

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


p1 = P2D(30, 40)
p2 = P2D(50, 10)

print(p1)

print(f"{p1} + {p2} = {p1 + p2}")
