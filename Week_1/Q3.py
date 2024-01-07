import math
list1=[]
list2=[]
dist = []
def add_coor(list,x_coor,y_coor):
    temp = [x_coor,y_coor]
    list.append(temp)
def euclidian_dist():
    if(len(list1) != len(list2)):
        print("Cant evaluate as the lsit sizes are different")
    else:
        for i,j in zip(list1,list2) :
            dist.append(math.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2))
            
        print(dist)    

print("Enter values in 1 for list 1, 2 for list 2, 3 for distances")
while(1):
    num = int(input("Enter choice"))
    if(num == 1):
        x_coor = int(input("Enter x coordinates: "))
        y_coor = int(input("Enter y coordinates: "))
        add_coor(list1,x_coor,y_coor)
    elif(num == 2):
        x_coor = int(input("Enter x coordinates: "))
        y_coor = int(input("Enter y coordinates: "))
        add_coor(list2,x_coor,y_coor)
    elif(num==3):
        euclidian_dist()
        break