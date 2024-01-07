import numpy as np
vertices = int(input("Enter number of vertices: "))

adj_list = {v: [] for v in range(1,vertices+1)}
adj_matrix = np.zeros((vertices,vertices))

def add_edge(u, v, weight):
    adj_list[u].append((v, weight))
    adj_matrix[u-1][v-1] = weight

def print_adj_list():
    print("Adjacency List:")
    print(adj_list)

def print_adj_matrix():
    print("Adjacency Matrix:")
    print(adj_matrix)


add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print_adj_list()
print()
print_adj_matrix()
