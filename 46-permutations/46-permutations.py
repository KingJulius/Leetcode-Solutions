class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def solve(perm):
            if len(nums) == len(perm):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                    solve(perm)
                    used[i] = False
                    perm.pop()
        solve([])
        return res
        
        