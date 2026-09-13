class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # [1,1*2,1*2*4,1*2*4*6] 


        # [-1,-1*0,-1*0*1,-1*0*1*2,-1*0*1*2*3]


        n = len(nums)
        res = [0] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        suf = 1
        for j in range(n-1,-1,-1):

            res[j] = suf*res[j]
            suf = suf*nums[j]
        return res
