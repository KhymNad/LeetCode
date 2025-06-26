from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])  # get size of matrix
        ans = []
        i, j = 0, 0 # pointers that iterate through matrix
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3  # values to deterimine current direction of pointers
        direction = RIGHT

        UP_WALL = 0 # This means: don’t go above row index 0, It's the top-most row.
        RIGHT_WALL = n  # len(matrix[0]) gives the index of the right wall
        DOWN_WALL = m # len(matrix) gives the index of the down wall
        LEFT_WALL = -1 # This means: don’t go to column index -1.is set that way because the leftmost valid column is at index 0, and going left past that would mean index -1

        while len(ans) != m*n: # once all values are within ans
            if direction == RIGHT:
                while j < RIGHT_WALL:   # iterate until you've hit the right wall
                    ans.append(matrix[i][j])
                    j += 1 # j increments through a row
                i, j = i+1, j-1 # once the right wall has been hit, we go down one row and back one row poition to stay within the matrix.
                RIGHT_WALL -= 1 # move the right wall left one column to prevent visiting the same indexes
                direction = DOWN # move down to continue spiral direction
            elif direction == DOWN:
                while i < DOWN_WALL:    # iterate until you hit bottom wall
                    ans.append(matrix[i][j])
                    i += 1  # increment i through the column
                i, j = i - 1, j - 1 # once the bottom wall is hit, move one column to the left and one row position to the left
                DOWN_WALL -= 1 # move the bottom wall up one row position to prevent visiting the same indexes
                direction = LEFT # spiral direction
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1  # decrement j through the row, move left
                i, j = i - 1, j + 1 # once left wall has been hit, move 1 column up and one row position to the right to stay in bounds
                LEFT_WALL += 1  # move the left wall one position to the right to prevent visiting the same indexes
                direction = UP  # spiral direction
            elif direction == UP:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1  # decrement i through the column, move up
                i, j = i + 1, j + 1 # once upper wall has been hit, move one row down, and one row position to the right 
                UP_WALL += 1 # move upper wall down
                direction = RIGHT # spiral direction

        return ans # TIME: O(m * n), SPACE: O(1)


