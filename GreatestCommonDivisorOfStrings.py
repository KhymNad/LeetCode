def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    end = False
    index = 0

    while not end:
        if (index < len(str1)) and (index < len(str2)) and (str1[index] == str2[index]):
            index += 1
        else:
            end = True
            return(str1[:index])
        
test1_str1 = "ABCABC"
test1_str2 = "ABC"

print(gcdOfStrings(test1_str1, test1_str2))