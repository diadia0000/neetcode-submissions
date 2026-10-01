class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        # print(nums)
        n = len(nums)
        for i in range(1,n):
            l = i-1
            r = i+1
            while (l>-1) and (r<n):
                #print(nums[l],nums[i],nums[r])
                if nums[l]+nums[i]+nums[r] == 0:
                    ans.add((nums[l],nums[i],nums[r]))
                    l-=1
                    r+=1
                elif nums[l]+nums[i]+nums[r] >0:
                    l-=1
                else:
                    r+=1
        # print(ans)
        return list(ans)