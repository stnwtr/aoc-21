import itertools
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @staticmethod
    def parse(raw: str):
        x, y = raw.split(',')
        return Point(int(x), int(y))


@dataclass(frozen=True)
class Line:
    a: Point
    b: Point

    def is_straight(self):
        return self.a.x == self.b.x or self.a.y == self.b.y

    def is_diagonal(self):
        return abs(self.a.x - self.b.x) == abs(self.a.y - self.b.y)

    def is_x_straight(self):
        return self.a.x == self.b.x

    def is_y_straight(self):
        return self.a.y == self.b.y

    def max_x(self):
        return self.a.x if self.a.x > self.b.x else self.b.x

    def max_y(self):
        return self.a.y if self.a.y > self.b.y else self.b.y

    def min_x(self):
        return self.a.x if self.a.x < self.b.x else self.b.x

    def min_y(self):
        return self.a.y if self.a.y < self.b.y else self.b.y

    def get_all_straight_points(self) -> list[Point]:
        if self.is_x_straight():
            return [Point(self.a.x, y) for y in range(self.min_y(), self.max_y() + 1)]
        elif self.is_y_straight():
            return [Point(x, self.a.y) for x in range(self.min_x(), self.max_x() + 1)]
        return []

    def get_all_diagonal_points(self) -> list[Point]:
        if not self.is_diagonal():
            return []
        if self.a.x == self.a.y:
            return [Point(x, x) for x in range(self.min_x(), self.max_x() + 1)]
        elif self.a.x == self.b.y:
            return [Point(self.min_x() + x, self.max_x() - x) for x in range(self.max_x() - self.min_x() + 1)]
        else:
            if self.a.x > self.b.x and self.a.y > self.b.y:  # 4,2 -> 3,1
                return [Point(self.a.x - x, self.a.y - x) for x in range(self.a.x - self.b.x + 1)]
            elif self.a.x > self.b.x and self.a.y < self.b.y:  # 4,1 -> 3,2
                return [Point(self.a.x - x, self.a.y + x) for x in range(self.a.x - self.b.x + 1)]
            elif self.a.x < self.b.x and self.a.y > self.b.y:  # 3,2 -> 4,1
                return [Point(self.a.x + x, self.a.y - x) for x in range(self.b.x - self.a.x + 1)]
            elif self.a.x < self.b.x and self.a.y < self.b.y:  # 3,1 -> 4,2
                return [Point(self.a.x + x, self.a.y + x) for x in range(self.b.x - self.a.x + 1)]

    @staticmethod
    def parse(raw: str):
        a, b = raw.split(' -> ')
        return Line(Point.parse(a), Point.parse(b))


def part1(lines):
    straight_lines = list(filter(lambda line: line.is_straight(), lines))
    straight_points = list(itertools.chain(*[line.get_all_straight_points() for line in straight_lines]))
    counter = Counter(straight_points).values()
    return len(counter) - len([x for x in counter if x == 1])


def part2(lines):
    straight_lines = list(filter(lambda line: line.is_straight(), lines))
    straight_points = list(itertools.chain(*[line.get_all_straight_points() for line in straight_lines]))
    diagonal_lines = list(filter(lambda line: line.is_diagonal(), lines))
    diagonal_points = list(itertools.chain(*[line.get_all_diagonal_points() for line in diagonal_lines]))
    counter = Counter(straight_points + diagonal_points).values()
    return len(counter) - len([x for x in counter if x == 1])


if __name__ == '__main__':
    with open('input/05.txt', 'r') as f:
        parsed_lines = [Line.parse(line) for line in f.readlines()]
    print(part1(parsed_lines))
    print(part2(parsed_lines))
