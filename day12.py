from dataclasses import dataclass


@dataclass
class Link:
    start: str
    end: str

    def __iter__(self):
        return iter((self.start, self.end))


class Graph:
    def __init__(self):
        self.graph = {}

    def add_link(self, link: Link):
        self.graph.setdefault(link.start, []).append(link.end)
        self.graph.setdefault(link.end, []).append(link.start)

    def add_links(self, links: list[Link]):
        for link in links:
            self.add_link(link)

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        return self.graph[item]


def find_paths(graph: Graph, start: str, end: str, path: list[str], day: int) -> list[list[str]]:
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for start in graph[start]:
        if start.islower() and start in path:
            if day == 2:
                doubles = len([p for p in path if p.islower() and path.count(p) == 2])
                if start in ('start', 'end') or doubles > 0:
                    pass
                else:
                    new_paths = find_paths(graph, start, end, path, day)
                    for new_path in new_paths:
                        paths.append(new_path)
        else:
            new_paths = find_paths(graph, start, end, path, day)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def part1(links: list[Link]) -> int:
    graph = Graph()
    graph.add_links(links)
    return len(find_paths(graph, 'start', 'end', [], 1))


def part2(links: list[Link]) -> int:
    graph = Graph()
    graph.add_links(links)
    return len(find_paths(graph, 'start', 'end', [], 2))


def main():
    with open('input/12.txt', 'r') as f:
        links = [Link(*link) for link in [link.split("-") for link in f.read().split()]]
    print(part1(links))
    print(part2(links))


if __name__ == '__main__':
    main()
