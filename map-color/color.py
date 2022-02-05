"""Solve map coloring with three colors."""


def read_file():
    adjacencies = {}
    lines = [l.strip() for l in open("./map.txt", "r").readlines()]
    for node in lines[0].split(" "):
        adjacencies[node] = set()
    for edge in lines[1:]:
        a, b = edge.split(" ")
        adjacencies[a].add(b)
        adjacencies[b].add(a)
    return adjacencies


def main():
    graph = read_file()
    print(graph)


if __name__ == "__main__":
    main()
