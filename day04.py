class Board:
    def __init__(self, id, file):
        self.id = id
        file.readline()
        raw_string_board = ''.join([file.readline() for _ in range(5)]).replace('\n', ' ').split()
        raw_board = list(map(int, raw_string_board))
        self.board = {key: False for key in raw_board}

    def mark(self, number):
        if number in self.board:
            self.board[number] = True

    def check(self) -> bool:
        values = list(self.board.values())

        for i in range(5):
            row = values[i * 5:i * 5 + 5]
            column = values[i::5]
            if all(row) or all(column):
                return True

        return False

    def get_unmarked(self):
        return [x for x in self.board if not self.board[x]]


def part1(inputs, boards):
    for number in inputs:
        for board in boards:
            board.mark(number)
            if board.check():
                return sum(board.get_unmarked()) * number


def part2(inputs, boards):
    not_checked_ids = [board.id for board in boards]
    for number in inputs:
        for board in boards:
            board.mark(number)
            if board.check() and board.id in not_checked_ids:
                if len(not_checked_ids) == 1:
                    return sum(board.get_unmarked()) * number
                else:
                    not_checked_ids.remove(board.id)


if __name__ == '__main__':
    with open('input/04.txt') as f:
        inputs = list(map(int, f.readline().split(',')))
        boards = [Board(x, f) for x in range(100)]

    print(part1(inputs, boards))
    print(part2(inputs, boards))
