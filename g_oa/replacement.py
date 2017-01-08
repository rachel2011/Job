import math

class Solution(object):
    def get_min(self, n):
        if n < 10:
            return n
        s = str(n)
        finalVal = int(s[:len(s)-1])
        for i in range(len(s)-1):
            tmp = s[:i] + str(max(int(s[i]), int(s[i+1]))) + s[i+2:]
            finalVal = min(int(tmp), finalVal)
        return finalVal

    def get_max(self, n):
        if n < 10:
            return n
        s = str(n)
        finalVal = 0
        for i in range(len(s) - 1):

            # tmp = s[:i] + str(math.ceil((int(s[i]) + int(s[i + 1])) / 2.0)) + s[i + 2:]
            tmp = s[:i] + str(int(math.ceil((int(s[i]) + int(s[i+1])) / 2.0))) + s[i + 2:]
            finalVal = max(int(tmp), finalVal)
        return finalVal

    def get_max_2(self, n):
        s = str(n)
        finalVal = 0
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                tmp = s[:i+1] + s[i + 2:]
                finalVal = max(int(tmp), finalVal)
        return finalVal

if __name__ == "__main__":
    n1 = 233614
    n2 = 11
    n3 = 623315
    n4 = 223336226
    n5 = 8
    obj = Solution()
    print(obj.get_min(n1))
    print(obj.get_min(n2))
    print(obj.get_min(n3))
    print(obj.get_min(n4))
    print(obj.get_min(n5))
    print()

    print(obj.get_max(n1))
    print(obj.get_max(n2))
    print(obj.get_max(n3))
    print(obj.get_max(n4))
    print()

    print(obj.get_max_2(n1))
    print(obj.get_max_2(n2))
    print(obj.get_max_2(n3))
    print(obj.get_max_2(n4))