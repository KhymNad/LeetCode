def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    index = 0
    moves = 0

    while index != len(nums) and moves != len(nums):
        if nums[index] == 0:
            item = nums.pop(index)
            nums.append(item)
            index -= 1
        index += 1
        moves += 1

    return(nums)

nums1 = [0,1,0,3,12]
nums2 = [0,0,1]

print(moveZeroes(nums2))