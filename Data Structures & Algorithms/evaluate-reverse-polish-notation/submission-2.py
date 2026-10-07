class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:
            if i in {"+","-","*","/"}:
                left = int(stack.pop())
                right = int(stack.pop())
                if i == "+":
                    stack.append(right+left)
                elif i == "-":
                    stack.append(right-left)
                elif i == "*":
                    stack.append(left*right)
                else:
                    stack.append(right / left)
            else:
                stack.append(i)
        return int(stack[0])