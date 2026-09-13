from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        step = 0
        for i in nums:
            if i-1 not in check:
                l = 1
                while i+l in check:
                    l+=1
                step = max(step,l)
        return step 
                        