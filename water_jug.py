import heapq
capacity = [3,5]
visited = []
buffer = [(0,0,[(0,0)])] #(3,5)

def getNeighbours(jug1,jug2,path):
    next_states = [(0, jug2), (jug1, 0), (capacity[0], jug2), (jug1, capacity[1]), 
                       (min(jug1 + jug2, capacity[0]), max(0, jug1 + jug2 - capacity[0])), 
                       (max(0, jug1 + jug2 - capacity[1]), min(jug1 + jug2, capacity[1]))]
    for state in next_states:
        if state not in visited:
            heapq.heappush(buffer,(state[0],state[1],path+[state]))


def solve():
    while True:
        jug1,jug2,path = heapq.heappop(buffer)
        if jug1==4 or jug2 == 4:
            print("solution found")
            print(path)
            return
        visited.append((jug1,jug2))
        getNeighbours(jug1,jug2,path)

solve()