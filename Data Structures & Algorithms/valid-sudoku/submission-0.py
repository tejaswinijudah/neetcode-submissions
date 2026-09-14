class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        for square in range(9):
            seen =  set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
#For every row:
#   create empty set

#    For every cell:
#       if empty:
 #           skip

 #       if number already in set:
 #           invalid Sudoku

  #      add number to set 
  # same goes for column and square also but for square u need to calculate the internal rows and columns of each 3 x 3 square
# square       0  1  2 | 3  4  5 | 6  7  8
#square//3     0  0  0 | 1  1  1 | 2  2  2
# This tells us which group of 3 rows the square belongs to.

#Multiply by 3:
#(square // 3) * 3
#square 0 → row 0
#square 1 → row 0
#square 2 → row 0

#square 3 → row 3
#square 4 → row 3
#square 5 → row 3

#square 6 → row 6
#square 7 → row 6
#square 8 → row 6

#So: (square // 3) * 3

# means: Find the first row of this 3×3 square.


# for column:
# square      0  1  2 | 3  4  5 | 6  7  8
# square%3    0  1  2 | 0  1  2 | 0  1  2
#This tells us which group of 3 columns the square belongs to.

#Multiply by 3:

#(square % 3) * 3

#gives the starting column:
#square 0 -> col 0
#square 1 → col 3
#square 2 → col 6

#square 3 → col 0
#square 4 → col 3
#square 5 → col 6

#square 6 → col 0
#square 7 → col 3
#square 8 → col 6

#So:   #(square % 3) * 3

#means: #Find the first column of this 3×3 square.
# row = (square//3) * 3 + i
#col = (square % 3) * 3 + j

#The first part finds the starting position of the square.

#Then i and j move around inside that square.
#
# so basically we got the starting row and column of each square and using that we just add the  loop from 0 to 2 and get the exact row and column within each square.
#
#row = block_start_row + local_row
#col = block_start_col + local_col

#block_start_row = (square // 3) * 3
#block_start_col = (square % 3) * 3

#    0  1  2
#    0  1  2 
#    0  1  2 
# this is the entire board split into 9 squares and 0 to 2 represent the columns. the squares if considered as 1 unit, then entire board is just a 
# 3 x 3 matrix.
# so we got this by doing square%3 to determine which of those squares come under which columns. 
# then we do (square%3) * 3, now this will give the actual starting columns of each sqaure.

#   0   3   6
#   0   3   6
#   0   3   6
#
# now we have the starting column of each square. then we add j (0 to 2) to each starting column to move inside each sqaure with the actual columns of the board
#   0th column = 0+0, 0+1, 0+2 = 0, 1, 2. all these 3 columns belong to sqaure 0. - first for loop tells us that. for square in range(9)
#   3rd column = 3+0, 3+1, 3+2 = 3, 4, 5. all these 3 columns belong to sqaure 1
# and so on... 
# this keeps repeating for all squares. square 0 and square 3 and square 6 all share the same columns although it is computed each time. as shown above.
# same shit is repeated for rows. 





