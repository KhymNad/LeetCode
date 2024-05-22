def gcdOfStrings(str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        end = False
        index = 0
        gcd = " "

        while (str1[index] == str2[index]) and (gcd[0] != str1[index]):
            gcd[index] = str1[index]
            index += 1


        # while not end:
        #     if (index < len(str1)) and (index < len(str2)) and (str1[index] == str2[index]):
        #         index += 1
        #     else:
        #         end = True
        #         gcd += str1[:index]
        #         #return(str1[:index])
        # if index == 0:
        #     return("")
        # for i in range(1,len(gcd)):
        #     if (gcd + (i*gcd)) != str1:
        #         gcd = gcd[:(index//2 * i)]
        #     else: 
        #         gcd = gcd[:index]
        
test1_str1 = "ABCABC"
test1_str2 = "ABC"

test2_str1 = "ABABAB"
test2_str2 = "ABAB"

test3_str1 = "LEET"
test3_str2 = "CODE"

test4_str1 = "ABCDEF"
test4_str2 = "ABC"

print(gcdOfStrings(test4_str1, test4_str2))