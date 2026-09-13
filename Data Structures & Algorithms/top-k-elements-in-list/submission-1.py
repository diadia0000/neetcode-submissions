from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numc = Counter(nums)
        ans = [i[0] for i in numc.most_common(k)]
        return ans