class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Map = {}
        for i in nums:
            if i not in Map:
                Map[i] = 1
            else:
                return True
        return False
