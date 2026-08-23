class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                t1=stack.pop()
                t2=stack.pop()
                if ch=="+":
                    stack.append(t1+t2)
                elif ch=="-":
                    stack.append(t2-t1)
                elif ch=="*":
                    stack.append(t1*t2)
                else:
                    stack.append(int(t2/t1))
        return stack[-1]

        