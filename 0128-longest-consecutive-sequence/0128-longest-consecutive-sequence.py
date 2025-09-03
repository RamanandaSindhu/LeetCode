
        
class Solution:
    def longestConsecutive(self, nums:List[int])->int:
        lookup = set(nums)
        longest = 0
        for n in lookup:
            if n-1 not in lookup:
                length = 1
                while n+1 in lookup:
                    length+=1
                    n = n+1
                longest = max(longest, length)
        return longest