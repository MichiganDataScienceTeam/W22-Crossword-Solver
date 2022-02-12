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

def color_graph(graph):
    colors = {}
    for node in graph:
        c = ["red", "blue", "green"]
        for edge in graph[node]:
            if edge in colors.keys():
                if colors[edge] in c:
                    c.remove(colors[edge])
        colors[node] = c[0]
    return colors
    
def main():
    graph = read_file()
    colors = color_graph(graph)
    print(colors)


if __name__ == "__main__":
    main()
