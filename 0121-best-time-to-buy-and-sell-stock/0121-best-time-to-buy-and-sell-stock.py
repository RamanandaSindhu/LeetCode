class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i, j = 0, 1
        while i<=j and j <len(prices):
            result = max(result, prices[j]-prices[i])
            # print(result)
            if prices[i]>prices[j]:
                i+=1
            else:
                j+=1
        return result