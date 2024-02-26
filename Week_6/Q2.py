import random

def random_board():
    """Generate a random 8-queens board."""
    return [random.randint(0, 7) for _ in range(8)]

def attacking_queens(board):
    """Count the number of attacking queens."""
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def hill_climbing():
    """Solve the 8-queens problem using hill climbing."""
    current_board = random_board()
    current_attacks = attacking_queens(current_board)

    while current_attacks > 0:
        # Generate all neighboring boards
        neighbors = []
        for i in range(8):
            for j in range(8):
                if j != current_board[i]:
                    neighbor = list(current_board)
                    neighbor[i] = j
                    neighbors.append(neighbor)

        # Choose the best neighboring board
        best_neighbor = current_board
        best_attacks = current_attacks
        for neighbor in neighbors:
            attacks = attacking_queens(neighbor)
            if attacks < best_attacks:
                best_neighbor = neighbor
                best_attacks = attacks

        # If there's no better neighbor, we've reached a local minimum
        if best_attacks >= current_attacks:
            break

        # Move to the best neighbor
        current_board = best_neighbor
        current_attacks = best_attacks

    return current_board

def print_board(board):
    """Print the board."""
    for row in range(8):
        line = ['Q' if board[row] == col else '.' for col in range(8)]
        print(' '.join(line))
    print()

if __name__ == "__main__":
    solution = hill_climbing()
    print("Solution found:")
    print_board(solution)

