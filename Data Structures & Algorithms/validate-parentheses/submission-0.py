class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            if c in "([{":
                stack.append(c)

            else:

                if stack == []:
                    return False

                match c:

                    case ')':
                        if stack.pop() != '(':
                            return False

                    case ']':
                        if stack.pop() != '[':
                            return False

                    case '}':
                        if stack.pop() != '{':
                            return False

        return len(stack) == 0