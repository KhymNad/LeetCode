## 74. Search a 2D Matrix (Medium)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n # indexes for flattened matrix
        l = 0
        r = t - 1 # position of the last index item of flattened version of matrix

        while l <= r:
            m = (l+r) // 2  # mid in flattened matrix
            i = m // n # row index
            j = m % n # column index

            mid_num = matrix [i][j] # actual middle number

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else: # target > mid_num
                l = m + 1
        
        return False

        # TIME: O(log (m*n))
        # SPACE: O(1)

