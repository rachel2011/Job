def canPermutePalindrome(string):
    string = string.strip()
    dic = {}
    #count how many times each char appears
    for letter in string:
        dic[letter] = dic.get(letter, 0) + 1
    """
    numberOfOdd = 0
    for letter2 in dic.values():
        if letter2 % 2 == 1:
            numberOfOdd += 1
        if numberOfOdd > 1:
            return False
    return True
    """
    # iterate through the dict and ensure that no more than one char has odd count
    return sum(v % 2 for v in dic.values()) < 2


string ='tactcoa'
print canPermutePalindrome(string)



