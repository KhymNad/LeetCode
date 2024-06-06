def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    p1 = 0  # pointer 1 
    p2 = k  # pointer 2
    maxAvg = 0
    sum = 0
    
    while p2 != len(nums):
        for i in range(p1,p2): # add all integers within the subarray
            sum += nums[i]
            print(sum)
        sum /= 4
        print(sum)

        if sum > maxAvg:
            maxAvg = sum

        p1 += 1
        p2 += 1

    return maxAvg

nums1 = [1,12,-5,-6,50,3]
k1 = 4

print(findMaxAverage(nums1, k1))