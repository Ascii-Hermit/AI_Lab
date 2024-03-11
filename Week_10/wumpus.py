import random

def generate_map(map_size):

	pit_num = random.randint(0,map_size/2)
	wumpus_num = random.randint(0,map_size/2)
	for i in range(pit_num):

		pit_row = random.randint(0,3)
		pit_col = random.randint(0,3)

		if(pit_row-1>=0):
			map[pit_row -1][pit_col] = -2 #-2 is for breeze
		if(pit_row+1<=map_size-1):
			map[pit_row +1][pit_col] = -2
		if(pit_col-1>=0):
			map[pit_row ][pit_col - 1] = -2
		if(pit_col+1<=map_size-1):
			map[pit_row][pit_col + 1] = -2


	wumpus_row = random.randint(0,3)
	wumpus_col = random.randint(0,3)

	map = [[0 for i in range (0,4)] for i in range(0,4)]

	map[pit_row][pit_col] = -1
	map[wumpus_row][wumpus_col] = 1

	map[wumpus_row -1][wumpus_col] = -3 #-3 is for stench
	map[wumpus_row +1][wumpus_col] = -3
	map[wumpus_row ][wumpus_col - 1] = -3
	map[wumpus_row][wumpus_col + 1] = -3

def check_percept(user_row,user_col):
	if (map[user_row][user_col] == -1):
		print("You fell in pit. Game over")
		return
	elif (map[user_row][user_col] == 1):
		print("Wumpus ate you. Game over")
		return
	elif (map[user_row][user_col] == -2):
		print("You encounter breeze")
	elif (map[user_row][user_col] == -1):
		print("You encounter stench")

generate_map(4)

while(True):
	print("You are at (0,0)")
	user_row = 0
	user_col = 0
	move = input("enter up down left right")
	if(move == 'up' & user_col+1<=3):
		user_col= user_col + 1
		check_percept(user_row,user_col)
	elif(move == 'down' & user_col-1<=0):
		user_col= user_col - 1
		check_percept(user_row,user_col)
	elif(move == 'left' & user_row-1<=0):
		user_row= user_row - 1
		check_percept(user_row,user_col)
	elif(move == 'right' & user_row+1<=3):
		user_row= user_row + 1
		check_percept(user_row,user_col)
	else:
		print("Invalid input")
