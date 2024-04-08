import random

# # f(x) = x^2 + 10
# def function_val(x):
#     return x*x + 20

# def climb():
#     count = 0 
#     iterations = 100
#     x_val = random.randint(-9,10)
#     func_val = function_val(x_val)
    

#     while count<iterations:
#         print(count)
#         step = random.randint(-1,1)
#         new_x_val = step + x_val
#         if not new_x_val >10 or new_x_val<-10:
#             new_func_val = function_val(new_x_val)
#             if(new_func_val>func_val):
#                 func_val = new_func_val
#                 x_val = new_x_val
#         count = count + 1
#     print(f"Solution converged at: {x_val} with a solution of {func_val}")

# climb()

###############################################

# def generateBoard():
#     board = [random.randint(0,7)for _ in range(8)]
#     return board

# def get_cost(board):
#     n = len(board)
#     cost = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
#                 cost += 1
#     return cost


# def climb():
#     curr_board = generateBoard()
#     curr_score = get_cost(curr_board)
#     count = 0
#     while curr_score>0:
#         print(count)
#         new_board = list(curr_board)
#         for col in range(8):
#             for row in range(8):
#                 if curr_board[col]!=row:
#                     new_board[col] = row
#                     next_score = get_cost(new_board)
#                     if next_score<curr_score:
#                         curr_board = list(new_board)
#                         curr_score = next_score
#                         break
#         if curr_score == get_cost(curr_board): # Stuck in local minima
#             curr_board = generateBoard()
#             curr_score = get_cost(curr_board)
#         count = count + 1
#     printBoard(curr_board)

# def printBoard(board):
#     game_board =[[0 for _ in range(8)]for _ in range(8)]
#     for i in range(8):
#         game_board[i][board[i]] = 1
#     print(game_board)

# climb()

#######################
# import random

# def generate_board(n):
#     return [random.randint(0, n-1) for _ in range(n)]

# def get_cost(board):
#     n = len(board)
#     cost = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
#                 cost += 1
#     return cost

# def hill_climb(n):
#     current_board = generate_board(n)
#     current_cost = get_cost(current_board)
    
#     while current_cost > 0:
#         next_board = list(current_board)
#         for col in range(n):
#             for row in range(n):
#                 if current_board[col] != row:
#                     next_board[col] = row
#                     cost = get_cost(next_board)
#                     if cost < current_cost:
#                         current_board = list(next_board)
#                         current_cost = cost
#                         break
#         if current_cost == get_cost(current_board): # Stuck in local minima
#             current_board = generate_board(n)
#             current_cost = get_cost(current_board)
            
#     return current_board

# def print_board(board):
#     n = len(board)
#     for row in range(n):
#         line = ""
#         for col in range(n):
#             if col == board[row]:
#                 line += "Q "
#             else:
#                 line += ". "
#         print(line)
        
# if __name__ == "__main__":
#     n = 8  # Change n to the desired board size
#     solution = hill_climb(n)
#     print("Solution:")
#     print_board(solution)

size = 5

def generate_board(size):
    return [random.randint(0,size-1) for _ in range(size)]

def get_score(board,size):
    cost = 0
    for i in range(size):
        for j in range(i+1,size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j-i:
                cost = cost + 1
    return cost


def solve(size):
    curr_board = generate_board(size)
    curr_score = get_score(curr_board,size)
    count = 0
    
    while curr_score>0:
        count = count + 1
        print(count)
        improved = False

        new_board=list(curr_board)
        for col in range(size):
            for row in range(size):
                if curr_board[col] !=row:
                    new_board[col] = row
                    new_cost = get_score(new_board,size)
                    if new_cost<curr_score:
                        curr_board = list(new_board)
                        curr_score = new_cost
                        improved = True
                        break
            if improved:
                break
        if not improved:
           curr_board = generate_board(size)
           curr_score = get_score(curr_board,size)

    printBoard(curr_board,size)
def printBoard(board,size):
    game_board =[[0 for _ in range(size)]for _ in range(size)]
    for i in range(size):
        game_board[i][board[i]] = 1
    print(game_board)


solve(size)


    
