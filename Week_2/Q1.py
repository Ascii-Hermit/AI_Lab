vertices = int(input("Enter the total number of vertices"))
adj_list = {v:[] for v in range(0,vertices)}
def add_edge(start,end):
    adj_list[start].append([start,end])
def display_graph():
    for i in adj_list.values():
        for val in i:
            print(val[0],"-->",val[1],end = " " )
        print()
add_edge(0,1)
add_edge(1,2)   
add_edge(2,0)
add_edge(2,1)
add_edge(3,2)
add_edge(4,5)
add_edge(5,4)
display_graph()
