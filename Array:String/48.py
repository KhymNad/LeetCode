from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose
        # swap i, js
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflection
        for i in range(n):
            for j in range(n // 2): # intuition is that n // 2 gives the index for the reflection line so for n = 3, 3//2 = 1 so reflection line is at index=1, we reflect along that index
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j] # the intuition here is that i is the left pointer and n-j-1 is the right pointer that is pressing into the reflection line/index and both correspond to the items being swapped/reflected

        # TIME: O(n^2)
        # SPACE: O(1)


        