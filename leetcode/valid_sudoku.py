# Q36. Valid sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

def isValidSudoku(board):
    board_length = len(board)
    kernal_size = 3 
    
    # Check sub-board rule: TC: O(N^2) = O(N); SC: O(n)
    # Have a 3x3 sliding window to extract each sub board, and check if 
    # they satisfy the rule.
    for i in range(0, board_length, kernal_size):
        for j in range(0, board_length, kernal_size):
            sub_board = []
            for r in range(i, i+kernal_size):
                sub_board.extend(board[r][j:j+3])
            if check_valid(sub_board) == False:
                return False 
    
    # Check row rule: TC: O(N^2); SC: O(N)
    for row in range(board_length):
        if check_valid(board[row]) == False:
            return False 
    
    # Check column rule: TC: O(N^2); SC: O(N) 
    for col in range(board_length):
        col_nums = [board[i][col] for i in range(board_length)]
        if check_valid(col_nums) == False:
            return False 
        
    return True 


def check_valid(arr):
    check_arr = []
    for n in arr:
        if n == '.':
            continue
        else: 
            if n not in check_arr:
                check_arr.append(n)
            else:
                return False 
                            
            

        

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    
print(isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board))