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

def check(node, values, value, adjacencies):
    for neighbor in adjacencies[node]:
        if values[neighbor] == value:
            return False
    return True

def try_this(node, values, adjacencies):
    for i in range(1, 4):
        if check(node, values, i, adjacencies):
            values[node] = i
            for neighbor in adjacencies[node]:
                if values[neighbor] == 0:
                    if not try_this(neighbor, values, adjacencies):
                        return False
    return values

def brute(adjacencies):
    values  = {}
    for node in adjacencies:
        values[node] = 0
    for node in adjacencies:
        print(try_this(node, values, adjacencies))

def main():
    graph = read_file()
    print(graph)
    brute(graph)


if __name__ == "__main__":
    main()
