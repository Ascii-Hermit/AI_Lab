import heapq
from collections import defaultdict
class Graph_Traversal:
    def __init__(self) -> None:
        self.graph = defaultdict()
        self.heuristic = defaultdict()

    def createHeuristics(self):
        for i in self.graph.keys():
            print(f"Heuristic for node {i}")
            heuristic = int (input())
            self.heuristic[i] = heuristic

    def Astar(self,graph,start,goal):
        frontier = [(0,start,[start])] #cost,curr_node,path
        visited = []
        while frontier:
            cost,curr_node,path = heapq.heappop(frontier)
            visited.append(curr_node)
            if curr_node == goal:
                return cost,path
            else:
                    for neighbours,neighbours_cost in graph[curr_node].items():
                        if neighbours not in visited:
                            heapq.heappush(frontier,(cost + neighbours_cost + self.heuristic[neighbours],neighbours,path+[neighbours] ))
    
    def UCS(self,graph,start,goal):
        frontier = [(0,start,[start])] #cost,curr_node,path
        visited = []
        while frontier:
            cost,curr_node,path = heapq.heappop(frontier)
            visited.append(curr_node)
            if curr_node == goal:
                return cost,path
            else:
                    for neighbours,neighbours_cost in graph[curr_node].items():
                        if neighbours not in visited:
                            heapq.heappush(frontier,(cost + neighbours_cost ,neighbours,path+[neighbours] ))
    
    def addEdge(self,start,dest,cost):
        temp_graph = {dest:cost}
        self.graph[start].update(temp_graph)

    def createGraph(self,num_nodes):
        for i in range(num_nodes):
            node = input(f"Enter the node {i}: ")
            self.graph[node]={}

# graph = {
#     'A':{'B':1,'C':9},
#     'B':{'C':9},
#     'C':{'D':3,'E':2},
#     'D':{'F':2},
#     'E':{'F':3},
# }
u = Graph_Traversal()
num_nodes = int(input("Enter the total numer of nodes: "))

u.createGraph(num_nodes)
u.addEdge('A','B',68)
u.addEdge('A','C',155)
u.addEdge('B','I',72)
u.addEdge('B','A',68)
u.addEdge('C','I',131)
u.addEdge('C','A',155)
u.addEdge('C','D',90)
u.addEdge('C','H',81)
u.addEdge('D','N',215)
u.addEdge('D','C',90)
u.addEdge('H','C',81)
u.addEdge('H','M',143)
u.addEdge('H','S',159)
u.addEdge('I','B',72)
u.addEdge('I','C',131)
u.addEdge('I','K',120)
u.addEdge('M','N',65)
u.addEdge('M','S',128)
u.createHeuristics()
start = 'A'
goal = 'N'
ucs_cost , ucs_path = u.UCS(u.graph,start,goal)
print(f"For UCS cost is {ucs_cost} and path taken is {ucs_path}")
astar_cost , astar_path = u.Astar(u.graph,start,goal)
print(f"For Astar cost is {astar_cost} and path taken is {astar_path}")