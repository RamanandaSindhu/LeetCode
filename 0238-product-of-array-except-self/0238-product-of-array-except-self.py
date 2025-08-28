class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        n = [1]*len(nums)
        prefix = 1
        for i in range(length):
            n[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(length-1, -1, -1):
            n[i] *= suffix
            suffix *= nums[i]


        return n 