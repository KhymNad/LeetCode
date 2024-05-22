def mergeStrings(word1, word2):
    mergedWord = ""
    index = 0
    longer = False

    while(not longer):
        if index < len(word1):
            mergedWord += word1[index]
        else:
            longer = True
            mergedWord += word2[index:]
            break
        
        if index < len(word2):
            mergedWord += word2[index]
        else: 
            longer = True
            mergedWord += word1[index+1:]
            break
        index += 1
        
    return(mergedWord)

test1_word1 = "abc"
test1_word2 = "pqr"

test2_word1 = "ab"
test2_word2 = "pqrs"

test3_word1 = "abcd"
test3_word2 = "pq"

print(mergeStrings(test3_word1, test3_word2))
