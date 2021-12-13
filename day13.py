from __future__ import annotations


class Paper:
    def __init__(self, points: set[tuple[int, int]]):
        self.points = points

    def fold(self, axis: str, index: int) -> Paper:
        points = []
        if axis == 'x':
            for point in self.points:
                if point[0] < index:
                    points.append(point)
                elif point[0] > index:
                    points.append((index - (point[0] - index), point[1]))
        elif axis == 'y':
            for point in self.points:
                if point[1] < index:
                    points.append(point)
                elif point[1] > index:
                    points.append((point[0], index - (point[1] - index)))
        return Paper(set(points))

    def _max_x(self):
        return max(point[0] for point in self.points)

    def _max_y(self):
        return max(point[1] for point in self.points)

    def __str__(self):
        grid = ''
        for y in range(self._max_y() + 1):
            for x in range(self._max_x() + 1):
                grid += '#' if (x, y) in self.points else '.'
            grid += '\n'
        return grid

    def __repr__(self):
        return self.__str__()


def part1(paper: Paper, folds: list[tuple[str, int]]) -> int:
    return len(paper.fold(*folds[0]).points)


def part2(paper: Paper, folds: list[tuple[str, int]]) -> int:
    for fold in folds:
        paper = paper.fold(*fold)
    return paper


def main():
    with open('input/13.txt', 'r') as f:
        raw_points, raw_folds = f.read().split('\n\n')
    points = [point.split(',') for point in raw_points.split()]
    points = list(map(lambda a: (int(a[0]), int(a[1])), points))
    folds = [fold.split('=') for fold in raw_folds.replace('fold along ', '').split()]
    folds = list(map(lambda a: (a[0], int(a[1])), folds))

    paper = Paper(set(points))

    print(part1(paper, folds))
    print(part2(paper, folds))


if __name__ == '__main__':
    main()
