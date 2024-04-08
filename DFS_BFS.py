# graph = {
#     'A':{'B':1,'C':9},
#     'B':{'C':9},
#     'C':{'D':3,'E':2},
#     'D':{'F':2},
#     'E':{'F':3},
#     'F':{}
# }
# class TopoSort:
#     def __init__(self):
#         self.indegree = { 
#                         'A':0,
#                         'B':0,
#                         'C':0,
#                         'D':0,
#                         'E':0,
#                         'F':0,
#                         }
#         self.graph = graph
#     def getIndegree(self):
#         for i in self.graph.keys():
#             for values in self.graph[i]:
#                 self.indegree[values] = self.indegree[values] + 1

#     def toposortDFS(self,start,goal):
#         stack = []
#         order = []
#         for i in self.indegree:
#             if self.indegree[i] == 0:
#                 stack.append(i)

#         while stack:
#             ele = stack.pop()
#             order.append(ele)
#             for i in self.graph[ele]:
#                 self.indegree[i] = self.indegree[i] - 1
#                 if self.indegree[i] == 0:
#                     stack.append(i)
#         return order



# def DFS(graph,start,goal):
#         frontier = []
#         explored = []
#         frontier.append(start)
#         while frontier:
#             node = frontier.pop()
#             if node == goal:
#                 explored.append(goal)
#                 return explored
#             explored.append(node)
#             for i in graph[node]:
#                 if i not in explored :
#                     frontier.append(i)

# def BFS(graph,start,goal):
#         frontier = []
#         explored = []
#         frontier.append(start)
#         while frontier:
#             node = frontier.pop(0)
#             if node == goal:
#                 explored.append(goal)
#                 return explored
#             explored.append(node)
#             for i in graph[node]:
#                 if i not in explored and i not in frontier:
#                     frontier.append(i)

# # print(f"DFS is {DFS(graph,'A','F')}")
# # print(f"BFS is {BFS(graph,'A','F')}")
# g = TopoSort()
# g.getIndegree()
# explored = g.toposortDFS('A','F')
# print(explored)




###########################################################

graph = {
    'A':['B','C'],
    'B':['C'],
    'C':['D','E'],
    'D':['F'],
    'E':['F'],
    'F':[]
}

inDegree = {
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'F':0    
}

goal = 'F'
start = 'A'

def dfs_search():
    frontier = [[start,(start)]]
    explored = []
    while(True):
        print("in")
        curr_node = frontier.pop()
        explored.append(curr_node[0])
        for nodes in graph[curr_node[0]]:
            if nodes == goal:
                print("Node found")
                return curr_node[1]
            if nodes not in explored:
                frontier.append([nodes,(curr_node[1]+nodes)])

def bfs_search():
    frontier = [[start,(start)]]
    explored = []
    while(True):
        print("in")
        curr_node = frontier.pop(0)
        explored.append(curr_node[0])
        for nodes in graph[curr_node[0]]:
            if nodes == goal:
                print("Node found")
                return curr_node[1]+nodes
            if nodes not in explored:
                frontier.append([nodes,(curr_node[1]+nodes)])


def getIndegree():
    for i in graph.keys():
        for nodes in graph[i]:
            inDegree[nodes] = inDegree[nodes] + 1


def topoSort():
    getIndegree()
    frontier = []
    sorted = []

    for i in inDegree.keys():
        if inDegree[i] == 0:
            frontier.append(i)

    while frontier:
        current = frontier.pop(0)
        sorted.append(current)
        for node in graph[current]:
            inDegree[node] = inDegree[node] - 1
            if inDegree[node] == 0:
                frontier.append(node) 
    print(sorted)

        






topoSort()


# path = dfs_search()
# print(path)
# path = bfs_search()
# print(path)

    
