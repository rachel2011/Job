class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        The most recent opening parenthesis must match the next closing symbol,
        if the entire string is processed and nothing is left on the stack, the string is correctly balanced
        Use a stack to store the chars, scan from the 1st to the last char in string s.
        ( [ { are free to push in the stack.
        When meets ) if stack top is (, then pop (.
        When meets ] if stack top is [, then pop [.
        When meets } if stack top is {, then pop {.
        Otherwise return false
        """
        stack = []
        balanced = True
        index = 0
        opens = "([{"
        closers = ")]}"
        while index < len(s) and balanced:
            symbol = s[index]
            if symbol in '([{':
                stack.append(symbol)
            else:
                # 如果stack为空：例如第一个符号就是右符号 "]]" 或者open close符号个数不等
                if not stack:
                    balanced = False
                else:
                    top = stack.pop()
                    if opens.index(top) != closers.index(symbol):
                        balanced = False
            index += 1

        if balanced and not stack:
            return True
        else:
            return False


