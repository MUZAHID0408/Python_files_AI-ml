N = int(input("Enter the  number of queens: "))
board = [[0]*N for _ in range(N)]
solutions = []
def is_safe(row, col):
    #check upper columns
    for i in range(0, row):
        if board[i][col] == ' q ':
            return False
        
    #check upper left diagona
    left_row = row - 1
    left_col = col - 1
    while(left_row >= 0 and left_col >=0):
        if board[left_row][left_col] == ' q ':
            return False
        left_row = left_row - 1
        left_col = left_col - 1

    #check upper right diagonal
    right_row = row - 1
    right_col = col + 1
    while(right_row >= 0 and right_col <= N-1):
        if board[right_row][right_col] == ' q ':
            return False
        right_col = right_col + 1
        right_row = right_row - 1     

    return True

def n_queens(row, n):
    if(n == 0):
        solution = []
        for row in board:
            solution.append(row.copy())
        solutions.append(solution)
        return True
    for j in range(0, N):
        if(is_safe(row, j)):
            board[row][j] = ' q ' 
            n_queens(row+1, n-1)
            board[row][j] = 0

n_queens(0, N)

print(f"Total solution found {len(solutions)}")