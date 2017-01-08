def solution(str1, length):
    str1 = list(str1)
    spaceCount = 0
    for i in range(length):
        if str1[i] == ' ':
            spaceCount += 1
    newLength = length + spaceCount * 2
    # return spaceCount, newLength
    for k in reversed(range(length)):
        if str1[k] == ' ':
            str1[newLength - 1] = '0'
            str1[newLength - 2] = '2'
            str1[newLength - 3] = '%'
            newLength -= 3
        else:
            str1[newLength - 1] = str1[k]
            newLength -= 1
    return ''.join(str1)


def solution_best(str1, length):
    str1 = list(str1)
    for i in range(length):
        if str1[i] == " ":
            str1[i] = "%20"
    return "".join(str1)


# Test

charArray, length = '1  ', 1
print solution(charArray, length)
print solution_best(charArray, length)

charArray, length = '          ', 2
print solution(charArray, length)
print solution_best(charArray, length)

charArray, length = ' a                    ', 4
print solution(charArray, length)
print solution_best(charArray, length)

charArray, length = 'abc      ', 3
print solution(charArray, length)
print solution_best(charArray, length)

charArray, length = 'abb a           ', 5
print solution(charArray, length)
print solution_best(charArray, length)