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


def solve(puzzle, adjacencies):
    for k in puzzle:
        if puzzle[k] is None:
            for color in [1, 2, 3]:
                neighboring = False
                for neighbor in adjacencies[k]:
                    if puzzle[neighbor] == color:
                        neighboring = True
                if neighboring:
                    continue
                puzzle[k] = color
                solve(puzzle, adjacencies=adjacencies)
            # puzzle[k] = None
    return puzzle

def main():
    graph = read_file()
    assignments = {k: None for k in graph}
    solved = solve(assignments, graph)
    print(solved)


if __name__ == "__main__":
    main()
