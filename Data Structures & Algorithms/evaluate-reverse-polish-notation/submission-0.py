import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(int(operations[token](left, right)))

        return stack[-1]