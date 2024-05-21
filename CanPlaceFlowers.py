def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    validSpots = 0

    for i in range(len(flowerbed)):
        if (i == 0) and len(flowerbed) > 1:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                validSpots += 1
        elif (i == len(flowerbed) - 1) and len(flowerbed) > 0:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                validSpots += 1
        else:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                validSpots += 1 
    print(validSpots)
    if validSpots == n:
        return True
    else:
        return False
    
flowerbed1 = [1,0,0,0,0,1]
flowerbed2 = [0]
n1 = 2

print(canPlaceFlowers(flowerbed1, n1))