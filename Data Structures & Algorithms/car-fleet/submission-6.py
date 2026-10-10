class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_pos = [(ind,i) for ind,i in enumerate(position)]
        new_pos.sort(key = lambda x:x[1],reverse=True)
        stack = []
        #print(new_pos)
        for i in new_pos:
            time = (target - i[1]) / speed[i[0]]
            #print(time)
            if not stack:
                stack.append(time)
                continue
            if time >stack[-1]:
                stack.append(time)
        return len(stack)