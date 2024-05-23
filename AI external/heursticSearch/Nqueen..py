def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    def print_solution(board):
        solution = []
        for i in range(n):
            row = ['.'] * n
            if board[i] != -1:
                row[board[i]] = 'Q'
            solution.append(' '.join(row))
        return solution

    result = []
    solve([-1] * n, 0)
    return result, print_solution

# Example usage:
n = 4
solutions, print_solution = solve_n_queens(n)

# Print all solutions
for sol in solutions:
    print("Solution:")
    for row in print_solution(sol):
        print(row)
    print("\n")