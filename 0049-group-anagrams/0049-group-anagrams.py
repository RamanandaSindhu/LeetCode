# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0]*26
#             for c in s:
#                 count[ord(c)-ord('a')]+= 1
#             res[tuple(count)].append(s)
#         return list(res.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str])->List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0]*26
#             for c in s:
#                 count[ord(c)-ord('a')]+=1
#             res[tuple(count)].append(s)
#         return list(res.values())


# class Solution:
#     def groupAnagrams(self, strs: List[str])-> List[List[str]]:
#         sortedS = []
#         res = defaultdict(list)
#         for s in strs:
#             c = ''.join(sorted(s))
#             #sortedS.append(c)
#             res[c].append(s)
#         return list(res.values())

class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            results[sorteds].append(s)
        return list(results.values())
