class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            m = (l+r)//2
            res = min(res, nums[m]) 
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res
                
        