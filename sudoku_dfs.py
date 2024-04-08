# def is_valid(board, row, col, num):
#     # Check if the number is already in the row
#     for i in range(9):
#         if board[row][i] == num:
#             return False
    
#     # Check if the number is already in the column
#     for i in range(9):
#         if board[i][col] == num:
#             return False
    
#     # Check if the number is already in the 3x3 box
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if board[i + start_row][j + start_col] == num:
#                 return False
    
#     return True

# def find_empty_location(board):
#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == 0:
#                 return row, col
#     return -1, -1

# def solve_sudoku(board):
#     row, col = find_empty_location(board)
#     if row == -1 and col == -1:
#         return True  # Puzzle is solved
    
#     for num in range(1, 10):
#         if is_valid(board, row, col, num):
#             board[row][col] = num
#             if solve_sudoku(board):
#                 return True
#             board[row][col] = 0  # Undo the assignment
    
#     return False

# def print_board(board):
#     for row in board:
#         print(" ".join(map(str, row)))

# if __name__ == "__main__":
#     # Example Sudoku board
#     sudoku_board = [
#         [5, 3, 0, 0, 7, 0, 0, 0, 0],
#         [6, 0, 0, 1, 9, 5, 0, 0, 0],
#         [0, 9, 8, 0, 0, 0, 0, 6, 0],
#         [8, 0, 0, 0, 6, 0, 0, 0, 3],
#         [4, 0, 0, 8, 0, 3, 0, 0, 1],
#         [7, 0, 0, 0, 2, 0, 0, 0, 6],
#         [0, 6, 0, 0, 0, 0, 2, 8, 0],
#         [0, 0, 0, 4, 1, 9, 0, 0, 5],
#         [0, 0, 0, 0, 8, 0, 0, 7, 9]
#     ]
    
#     if solve_sudoku(sudoku_board):
#         print("Solution:")
#         print_board(sudoku_board)
#     else:
#         print("No solution exists.")
#  #################################################
board = [[0 for _ in range(9)] for _ in range(9)]


def find_empty(board):
    for row in range(0,9):
        for col in range(0,9):
            if board[row][col] == 0:
                return row,col
    return -1,-1
            
def checkValid(board,row,col,num):
    for i in range(0,9):
        if board[row][i] == num:
            return False
    for i in range(0,9):
        if board[i][col] == num:
            return False
        
    start_row = 3*(row//3)
    start_col = 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True
            
def solve_sudoku(board):
    
    row,col = find_empty(board)
    if row == -1:
        print(board)
        return True
    for digit in range(1,10):
        print("in")
        if checkValid(board,row,col,digit):
            board[row][col] = digit
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

solve_sudoku(board)
    