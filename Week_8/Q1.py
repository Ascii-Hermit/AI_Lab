def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    print(words)
    unique_letters = set(''.join(words))
    print(unique_letters)
    
    if len(unique_letters) > 10:
        return None  # More than 10 unique letters, impossible to assign unique digits

    # Generate all possible permutations of digits for the unique letters
    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))

        # Check if the permutation satisfies the cryptarithmetic condition
        if all(mapping[word[0]] != 0 for word in words) and \
           sum(int(''.join(str(mapping[char]) for char in word)) for word in words[:-1]) == int(''.join(str(mapping[char]) for char in words[-1])):
            return mapping
    
    return None

# Example usage:
puzzle = "DONALD GERALD ROBERT"
solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
