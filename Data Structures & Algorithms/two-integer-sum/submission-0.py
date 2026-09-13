class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            Map[nums[i]] = i
        print(Map)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Map.keys() and Map[diff] != i:
                return [i,Map[diff]]
        return []

