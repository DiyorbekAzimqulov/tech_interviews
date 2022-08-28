class Solution:
    def isValid(self, s: str) -> bool:
        """
        we have two conditions
        incoming char (parenthesis) might be opening or closing
        if opening then next char if closing must be the opposite
        if it is closing then one before that char must be opening of the same type
        """
        match = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for char in s:
            if char not in match: # opening parenthesis
                stack.append(char)
            else: # closing parenthesis
                # to be valid, char must be top stack element's opposite parenthesis
                if len(stack) == 0:
                    return False
                if match[char] != stack.pop():
                    return False
        return len(stack) == 0
                

s = Solution()

print(s.isValid("{{}"))