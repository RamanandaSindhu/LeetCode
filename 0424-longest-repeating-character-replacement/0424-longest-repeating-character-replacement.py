class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        result =0
        for j in range(len(s)):
            count[s[j]]=1+count.get(s[j], 0)

            while (j-i+1)-max(count.values())>k:
                count[s[i]]-=1
                i+=1

            result = max(result, (j-i+1))
        return result