class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for c, m in sorted(zip(position, speed), reverse=True):
            x = float((target - c) / m)
            if stack and stack[-1] >= x:
                continue
            else:
                stack.append(x)
        return len(stack)