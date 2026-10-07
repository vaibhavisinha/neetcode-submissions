class Solution:
    def isValid(self, s: str) -> bool:
        close_braces_map = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in close_braces_map:
                if stack:
                    open_brace = stack.pop()
                    if open_brace != close_braces_map[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return not stack