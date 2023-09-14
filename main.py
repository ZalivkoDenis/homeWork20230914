# ШАГ. Д/з по сроку 14/09/2023
import math


def climbStairs(n: int) -> int:
    f1 = f2 = 1
    for _ in range(n - 1):
        f1, f2 = f2, f1 + f2
    return f2


def climbStairs_str(n: int) -> str:
    return f'Stairs count: {n},\tclimbs variants: {climbStairs(n)}'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def line_length(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def line_length_str(p1: Point, p2: Point) -> str:
    return f'A1[{p1.x}, {p1.y}],\tA2[{p2.x}, {p2.y}]:\t{round(line_length(p1, p2), 2)}'


if __name__ == '__main__':
    print(climbStairs_str(5))
    print(climbStairs_str(8))
    print(climbStairs_str(35))

    print('-' * 40)

    print(line_length_str(Point(15, 7), Point(22, 11)))
    print(line_length_str(Point(0, 0), Point(0, 0)))
    print(line_length_str(Point(0, 0), Point(1, 1)))

# Stairs count: 5,	climbs variants: 8
# Stairs count: 8,	climbs variants: 34
# Stairs count: 35,	climbs variants: 14930352
# ----------------------------------------
# A1[15, 7],	A2[22, 11]:	8.06
# A1[0, 0],	A2[0, 0]:	0.0
# A1[0, 0],	A2[1, 1]:	1.41
#
# Process finished with exit code 0