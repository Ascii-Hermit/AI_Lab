import itertools

def solve_cryptarithmetic(puzzle):
    letters = set(ch for ch in puzzle if ch.isalpha())
    if len(letters) > 10:
        return "Invalid puzzle: More than 10 distinct letters"
    
    unique_letters = ''.join(letters)
    if len(unique_letters) > 10:
        return "Invalid puzzle: More than 10 letters (digits)"

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = {ch: digit for ch, digit in zip(unique_letters, perm)}
        equation = puzzle.translate(str.maketrans(mapping))
        if eval(equation):
            return {ch: digit for ch, digit in zip(unique_letters, perm)}

    return "No solution found"

if __name__ == "__main__":
    puzzle = "SEND + MORE == MONEY"
    solution = solve_cryptarithmetic(puzzle)
    if isinstance(solution, dict):
        print("Solution found:")
        for ch, digit in solution.items():
            print(f"{ch}: {digit}")
    else:
        print(solution)
