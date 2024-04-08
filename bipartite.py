graph = {
    "A":["B"],
    "B":["C"],
    "C":["D"],
    "D":["E"],
    "E":["F"],
    "F":["G"],
    "G":["B"]
}
flag={
    "A":-1,
    "B":-1,
    "C":-1,
    "D":-1,
    "E":-1,
    "F":-1,
    "G":-1
}

start = "A"

def check_bipartite():
    frontier = [start]
    flag[start] = 0
    explored = []
    while frontier:
        curr_node = frontier.pop()
        explored.append(curr_node)
        for node in graph[curr_node]:
            if node not in explored:
                if flag[curr_node] == 0:
                    flag[node] = 1
                    frontier.append(node)
                if flag[curr_node] == 1:
                    flag[node] = 0
                    frontier.append(node)
            else:
                if flag[curr_node] == flag[node]:
                    print("Graph is not bipartite")
                    return
                
    print("Graph is bipartite")

check_bipartite()


