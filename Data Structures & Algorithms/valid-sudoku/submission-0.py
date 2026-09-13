class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check square
        for i in range(0,9,3):
            for j in range(0,9,3):
                check = [0]*10
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != "." and check[int(board[i+k][j+l])] == 0:
                            check[int(board[i+k][j+l])] = 1
                        elif board[i+k][j+l] != "." and check[int(board[i+k][j+l])] == 1:
                            return False
        # check row
        for i in range(9):
            check_row = [0]*10
            for j in range(9):
                if board[j][i] != "." and check_row[int(board[j][i])] == 0:
                    check_row[int(board[j][i])] = 1
                elif board[j][i] != "." and check_row[int(board[j][i])] == 1:
                    return False
        # check col
        for i in range(9):
            check_col= [0]*10
            for j in range(9):
                if board[i][j] != "." and check_col[int(board[i][j])] == 0:
                    check_col[int(board[i][j])] = 1
                elif board[i][j] != "." and check_col[int(board[i][j])] == 1:
                    return False
        return True

