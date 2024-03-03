class EightQueensProblem:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def is_safe(self, row, col):
        # Check if there is a queen in the same row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self):
        solutions = []
        self.solve_util(0, solutions)
        return solutions

    def solve_util(self, col, solutions):
        if col == self.n:
            solution = []
            for row in self.board:
                solution.append(row[:])
            solutions.append(solution)
            return True

        res = False
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve_util(col + 1, solutions) or res
                self.board[i][col] = 0  # Backtrack
        return res


def print_solution(solution):
    for row in solution:
        print(row)
    print()


if __name__ == "__main__":
    n = 8
    problem = EightQueensProblem(n)
    solutions = problem.solve()
    print(f"Total solutions for {n} queens problem:", len(solutions))
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        print_solution(solution)
