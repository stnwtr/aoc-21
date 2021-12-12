def adjacent_indices(index: int) -> list[int]:
    offsets = [-11, -10, -9, -1, 1, 9, 10, 11]
    if index % 10 == 0:
        offsets = [-10, -9, 1, 10, 11]
    elif (index - 9) % 10 == 0:
        offsets = [-11, -10, -1, 9, 10]
    return [index + offset for offset in offsets if 0 <= index + offset < 100]


def increase_energy_level(octopuses: list[int], index: int) -> int:
    flash_counter = 0
    octopuses[index] += 1
    if octopuses[index] == 10:
        flash_counter += 1
        adjacent = adjacent_indices(index)
        for i in adjacent:
            flash_counter += increase_energy_level(octopuses, i)
    return flash_counter


def calculate(octopuses: list[int], day: int) -> int:
    day_counter = 0
    flash_counter = 0
    while True:
        day_counter += 1
        for i in range(len(octopuses)):
            flash_counter += increase_energy_level(octopuses, i)
        if all([octopus >= 10 for octopus in octopuses]) and day == 2:
            return day_counter
        for i in range(len(octopuses)):
            if octopuses[i] >= 10:
                octopuses[i] = 0
        if day_counter == 100 and day == 1:
            return flash_counter


def main():
    with open('input/11.txt', 'r') as f:
        octopuses = [int(x) for x in ''.join(f.read().split())]
    print(calculate(octopuses.copy(), 1))
    print(calculate(octopuses.copy(), 2))


if __name__ == '__main__':
    main()
