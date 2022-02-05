"""Solve map coloring with three colors."""


def read_file():
    adjacencies = {}
    lines = [l.strip() for l in open("map-color/map.txt", "r").readlines()]
    for node in lines[0].split(" "):
        adjacencies[node] = set()
    for edge in lines[1:]:
        a, b = edge.split(" ")
        adjacencies[a].add(b)
        adjacencies[b].add(a)
    return adjacencies

def check(adjacencies, colors, node):
    for adj in adjacencies[node]:
        if (adj in colors) and colors[adj] == colors[node]:
            return False
    return True

def solve(adjacencies):
    options = [1, 2, 3]
    colors = {}
    for node, adj in adjacencies.items():
        colors[node] = options[0]
        if not check(adjacencies, colors, node):
            colors[node] = options[1]
        if not check(adjacencies, colors, node):
            colors[node] = options[2]
        for n in adj:
            for i in options:
                colors[n] = i
                if check(adjacencies, colors, n):
                    break
    return colors
    

def main():
    graph = read_file()
    print(graph)
    solved = solve(graph)
    for node, color in solved.items():
        print (node, " ", color)

if __name__ == "__main__":
    main()
