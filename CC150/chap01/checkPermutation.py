"""
Need to check:
1. if white space could be ignored
2. the size of charset
3. case sensitive
"""
def ispermutationSort(str1, str2):
    if len(str1) != len(str2):
        # if the strings are not same length, they cannot be
        # permutations
        return False
    if sorted(str1) == sorted(str2):
        return True
    return False

def ispermutationSort2(str1, str2):
    if len(str1) != len(str2):
        # if the strings are not same length, they cannot be
        # permutations
        return False
    charSet = [0]*128
    for char in str1:
        charSet[ord(char)] += 1

    for char in str2:

        if str2.count(char) == charSet[ord(char)]:
            return True
        return False
        """
        charSet[ord(char)] -= 1
        if charSet[ord(char)] < 0:
            return False
        """
    return True



# Test
str1, str2 = '', ''
print ispermutationSort(str1, str2), ispermutationSort2(str1, str2)

str1, str2 = 'a', ''
print ispermutationSort(str1, str2), ispermutationSort2(str1, str2)

str1, str2 = 'a', 'b'
print ispermutationSort(str1, str2), ispermutationSort2(str1, str2)

str1, str2 = 'abc', 'acb'
print ispermutationSort(str1, str2), ispermutationSort2(str1, str2)

str1, str2 = 'abccsbb', 'cabbbsc'
print ispermutationSort(str1, str2), ispermutationSort2(str1, str2)

str1, str2 = 'abccsbb', 'cabbbsk'
print ispermutationSort(str1, str2), ispermutationSort2(str1, str2)