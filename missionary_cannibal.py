import heapq

buffer = [(0,0,3,3,[(0,0,3,3)])] #RM, RC, LM, LC    
visited = []

def checkSafe(RM,RC,LM,LC):
    if RM>3 or RC>3 or LC>3 or LM>3 or RM<0 or RC<0 or LC<0 or LM<0 or LC>LM  or RM>LC:
        return False
    return True



def getNeighbours(RM,RC,LM,LC,path):
    next_state = [(RM+2,RC,LM-2,LC),(RM+1,RC+1,LM-1,LC-1),(RM,RC+2,LM,LC-2),(RM-2,RC,LM+2,LC),(RM-1,RC-1,LM+1,LC+1),(RM,RC-2,LM,LC-2),(RM,RC+1,LM,LC-1),(RM+1,RC,LM-1,LC),(RM-1,RC,LM+1,LC),(RM,RC-1,LM,LC+1)]
    for state in next_state:
        if state in visited and checkSafe(state[0],state[1],state[2],state[3]):
            new_path = path+[state]
            new_state = [state[0],state[1],state[2],state[3],new_path]
            buffer.append(new_state)
            

def solve():
    while True:
        
        node = buffer.pop()
        if node[0]==3 and node[1]==3:
            print("solution found")
            print(node[4])
            return
        visited.append((node[0],node[1],node[2],node[3]))
        getNeighbours(node[0],node[1],node[2],node[3],node[4])


solve()