class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:
                val,ind = stack.pop()
                result[ind] = i-ind
            stack.append((temperatures[i],i))
        return result


