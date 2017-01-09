# s2 will be a substring of s1s1
def strRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        if s2 in s1+s1:
            return True
    return False

# Test
s1 = ''
s2 = ''
print strRotation(s1, s2)

s1 = ''
s2 = 'a'
print strRotation(s1, s2)

s1 = 'a'
s2 = ''
print strRotation(s1, s2)

s1 = 'abc'
s2 = 'abc'
print strRotation(s1, s2)

s1 = 'leetcode'
s2 = 'tcodelee'
print strRotation(s1, s2)

s1 = 'leetcode'
s2 = 'tcodeele'
print strRotation(s1, s2)

s1 = 'leetcode'
s2 = 'tcodeleee'
print strRotation(s1, s2)