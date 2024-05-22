def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """

    result = []

    for i in range(len(candies)):
        for j in range(len(candies)):
            print(candies[j])
            if ((candies[i] + extraCandies) < candies[j]) and candies[i] != candies[j]: # breaks from the loop if false is found
                result.append(False)
                break
            elif j == len(candies)-1:
                result.append(True)
    return(result)

candies1 = [2,3,5,1,3]
extraCandies1 = 3

print(kidsWithCandies(candies1, extraCandies1))