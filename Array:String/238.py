from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The intuition is to traverse the list a single time with 2 pointers. One starting at the LHS (start of array) and one on the RHS (end of array). We initialize multipliers to 1 for the LHS and RHS inorder to multiply them by the integers in the array either coming from the LHS or the RHS, 1 is trivial. As LHS pointer and RHS pointer traverse the array thye multiply by the initial mulitplier leaving the LHS array to have values correspoinding to the LSH product values of what ever index and the RHS array to have values corresponding to the RHS product values of what ever index. Multiplying the LHS and RHS arrays results in the answer array that we want to return

        l_mult = 1  # LHS multiplier
        r_mult = 1  # RHS multiplier
        n = len(nums)   
        l_arr = [0] * n # initialis LHS array
        r_arr = [0] * n # initialize RHS array

        for i in range(n):
            j = -i -1   # j starts at end of nums and moves according to i, key to O(n) complexity
            l_arr[i] = l_mult # insert the current LHS multiplier in LHS array
            r_arr[j] = r_mult # insert the current RHS multiplier in RHS array
            l_mult *= nums[i] # calculate the new LHS multiplier
            r_mult *= nums[j] # calculate the new RHS multiplier

        # Multiply the two LHS and RHS array together ussing zip() function
        return [l * r for l, r in zip(l_arr, r_arr)]

        # Time: O(n)
        # Space: O(n) -- Suboptimal


