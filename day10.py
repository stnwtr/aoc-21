import functools
from dataclasses import dataclass


@dataclass
class ClosingSymbols:
    left: str
    right: str
    corrupted_score: int
    incomplete_score: int


symbols = [
    ClosingSymbols('(', ')', 3, 1),
    ClosingSymbols('[', ']', 57, 2),
    ClosingSymbols('{', '}', 1197, 3),
    ClosingSymbols('<', '>', 25137, 4)
]

ls = {s.left: s for s in symbols}
rs = {s.right: s for s in symbols}


def line_score(line: str) -> dict[int, int]:
    expected = []
    for c in line:
        if c in ls:
            expected.append(ls[c].right)
        elif c == expected[len(expected) - 1]:
            expected.pop()
        else:
            return {1: rs[c].corrupted_score, 2: -1}
    return {1: 0, 2: functools.reduce(lambda a, b: a * 5 + b, reversed([rs[e].incomplete_score for e in expected]), 0)}


def part1(lines: list[str]) -> int:
    return sum([line_score(line)[1] for line in lines])


def part2(lines: list[str]) -> int:
    scores = sorted(filter(lambda a: a != -1, [line_score(line)[2] for line in lines]))
    return scores[len(scores) // 2]


def main():
    with open('input/10.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
