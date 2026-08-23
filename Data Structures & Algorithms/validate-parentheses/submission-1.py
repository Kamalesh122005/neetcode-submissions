class Solution:
    def isValid(self, s: str) -> bool:
        vp={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack=[]
        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if not stack:
                    return False
                if stack[-1]!=vp[p]:
                    return False
                stack.pop()
        return not stack
        