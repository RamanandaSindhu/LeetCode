# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1+ count.get(num, 0)
        
#         Freq = [[]for i in range(len(nums)+1)]

#         for i,c in count.items():
#             Freq[c].append(i)

#         res =[]
#         for i in range(len(Freq)-1, 0, -1):
#             if Freq[i]:
#                 res.extend(Freq[i])
#                 if len(res)==k:
#                     return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int)-> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+ count.get(n,0)
        result = [[]for i in range(len(nums)+1)]
        for num, freq in count.items():
            result[freq].append(num)
        # print(result)

        r = []
        for i in range(len(result)-1,0,-1):
            if result[i]:
                r.extend(result[i])
                
                if len(r) == k:
                    return r