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

def colour(graph, colourDict):
    for node in graph:
        print("try node " + node)
        for i in range(3):
            isValid = True
            print("checking colour " + str(i))
            for j in graph[node]:
                print("Node adjacent node " + str(j))
                if colourDict[j] == i:
                    print(str(j) + " has colour " + str(colourDict[j])+ ", conflict")
                    isValid = False
                    break
                else:
                    print(str(j) + " has " + str(colourDict[j])+ ", no conflict")
            if isValid:
                colourDict[node] = i
                print("colour " + node + " " + str(i))
                break
    # colour(graph, node, colourDict)

def main():
    graph = read_file()

    colourDict = {}
    for node in graph:
        colourDict[node] = -1
    colour(graph, colourDict)
    print(graph)
    print(colourDict)


if __name__ == "__main__":
    main()
