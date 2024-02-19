

import heapq
import copy

class PuzzleNode:
    def __init__(self,puzzle,g):
        self.puzzle = puzzle
        self.g = g
        self.h = self.get_heuristic()
        self.cost = self.g + self.h
        self.path = []

    def __lt__(self,other):
        return self.cost<other.cost
    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def get_heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] != i*3+j:
                    count = count + 1
        return count
    
def get_neighbours(node,g):
    neighbours = []
    directions = [(1,0),(-1,0),(0,-1),(0,1)]
    zero_row, zero_col = 0,0
    for i in range(3):
        for j in range(3):
            if node.puzzle[i][j] == 0:
                zero_row = i
                zero_col = j
                break
    for row_inc,col_inc in directions:
        new_puzzle = copy.deepcopy(node.puzzle)
        new_row = 0 
        new_col = 0 
        new_row = row_inc + zero_row
        new_col = col_inc + zero_col
        if new_row>=0 and new_row<3 and new_col>=0 and new_col<3:
            new_puzzle[zero_row][zero_col] = new_puzzle[new_row][new_col]
            new_puzzle[new_row][new_col] = 0
            new_node = PuzzleNode(new_puzzle,node.g+1)
            neighbours.append(new_node)
    return neighbours




def astar(start,goal):
    frontier = [] 
    explored=[]
    g=0
    start_node = PuzzleNode(start,g)
    start_node.path.append(start)
    heapq.heappush(frontier,start_node)
    while frontier:
        node=heapq.heappop(frontier)
        explored.append(node)
        if node.puzzle == goal:
            return node.g
        for neighbours in get_neighbours(node,node.g):
            if neighbours not in explored:
                heapq.heappush(frontier,neighbours)


start = [[1,2,3],
         [4,0,5],
         [6,7,8]]

goal = [[0,1,2],
         [3,4,5],
         [6,7,8]]
    
steps = astar(start,goal)
print(f"The puzzle was solved in {steps} steps ")

