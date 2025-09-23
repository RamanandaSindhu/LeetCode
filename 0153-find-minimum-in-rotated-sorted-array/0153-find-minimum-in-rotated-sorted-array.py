class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        i, j = 0, len(nums)-1

        while i<=j:
            if nums[i]<=nums[j]:
                res = min(res, nums[i])
                break
            m = (i+j)//2
            res = min(res, nums[m])
            if nums[m]>=nums[i]:
                i = m+1
            else:
                j = m
        return res
