def compression(str1):
    finalString = ''
    previous = str1[:1]
    count = 1
    if str1 is None or len(str1) == 0 or len(str1) == 1: return str1
    for char in str1[1:]:
        if char == previous:
            count += 1
        else:
            finalString += previous + str(count)
            previous = char
            count = 1
    finalString += previous + str(count)
    if len(finalString) < str1:
        return finalString
    else:
        return str1

# Test
str1 = 'abcde'
print compression(str1)

str1 = 'aabccccaaa'
print compression(str1)

str1 = 'abccdee'
print compression(str1)

str1 = 'accc'
print compression(str1)

