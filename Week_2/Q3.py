adj_list = {}
index = {}
def add_edge(start_node,end_list):
    if(start_node not in adj_list.keys()):
        adj_list[start_node] = []
        for val in end_list:
            adj_list[start_node].append(val)
    else:
        for val in end_list:
            adj_list[start_node].append(val)

def make_index():
    ind = 0
    for val in adj_list.keys():
        index[val] = ind
        ind = ind +1
def display_adj_mat():
    for start in adj_list.keys():
        for val in adj_list[start]:
            adj_mat[index.get(start)][index.get(val)] = 1
    print(adj_mat)

def display_adj_list():
    print(adj_list)

add_edge("A",["B","C","E"])
add_edge("B",["A","C"])
add_edge("C",["A","B","D","E"])
add_edge("D",["C"])
add_edge("E",["A","C"])
display_adj_list()
make_index()

adj_mat = [[0]*len(adj_list.keys()) for i in range(len(adj_list.keys()))]
display_adj_mat()

