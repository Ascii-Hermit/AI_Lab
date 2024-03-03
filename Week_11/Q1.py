import random

def generate_random_board():
    return [random.randint(0, 7) for _ in range(8)]

def calculate_attacks(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                attacks += 1
    return attacks

def get_next_neighbor(board):
    neighbors = []
    current_attacks = calculate_attacks(board)
    for col in range(8):
        for row in range(8):
            if board[row] != col:
                new_board = list(board)
                new_board[row] = col
                attacks = calculate_attacks(new_board)
                if attacks < current_attacks:
                    neighbors.append((new_board, attacks))
    return neighbors

def hill_climbing():
    current_board = generate_random_board()
    current_attacks = calculate_attacks(current_board)

    while True:
        neighbors = get_next_neighbor(current_board)
        if not neighbors:
            break
        
        min_attacks = min(neighbors, key=lambda x: x[1])[1]
        if min_attacks >= current_attacks:
            break
        
        current_board, current_attacks = random.choice([neighbor for neighbor in neighbors if neighbor[1] == min_attacks])

    return current_board, current_attacks

def main():
    solution, attacks = hill_climbing()
    print("Solution found with attacks:", attacks)
    for row, col in enumerate(solution):
        print("Row:", row + 1, " Column:", col + 1)

if __name__ == "__main__":
    main()
