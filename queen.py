def is_safe(board, row, col, n):
    # Check if there is a queen in the same column or diagonal
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_board(board):
    # Print the board (each queen is represented by 'Q')
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

def solve_n_queens_util(board, row, n):
    # If all queens are placed, return True
    if row == n:
        print_board(board)
        print("\n")
        return True

    res = False
    # Try all columns in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            res = solve_n_queens_util(board, row + 1, n) or res
            # Backtrack
            board[row] = -1
    
    return res

def solve_n_queens(n):
    # Initialize the board with -1 (indicating no queen is placed)
    board = [-1] * n
    
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
    else:
        print("Solutions found for N =", n)

# Take user input for n (the number of queens)
n = int(input("Enter the value of N (number of queens): "))
solve_n_queens(n)
