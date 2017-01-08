
def isUniqueChars(input):
    # O(n) time
    if len(input) > 128:
        return false
    charSet = [False] * 128
    for char in input:
        index = ord(char)
        if charSet[index]:
            return False
        charSet[index] = True
    return True

# Test
input = 'a'
print isUniqueChars(input)
input = 'abc'
print isUniqueChars(input)

input = 'asdfa'
print isUniqueChars(input)
