stack1 = []
stack2 = []
def enqueue(ele):
    stack1.append(ele)
def dequeue():
    if(len(stack1) == 0):
        print("Stack is empty")
    else:
        stack2.clear()
        for i in stack1:
            stack2.append(i)
        ele = stack2.pop()
        stack1.clear()
        for i in stack2:
            stack1.append(i)
        return ele
def display():
    print(stack1,"\n")
print("1>Enqueue, 2>Dequeue, 3>Display, 4>Exit")
while(1):
    num = int(input("Enter choice: "))
    if(num==1):
        ele = int(input("Enter number to enqueue: "))
        enqueue(ele)
    elif(num==2):
        print(f"The dequeued number is:{dequeue()}")
    elif(num==3):
       display()
    elif(num==4):
        break
    else:
        print("Invalid input")
