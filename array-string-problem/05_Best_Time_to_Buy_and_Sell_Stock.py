class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max_pro = 0
        for i in prices:
            if i<min:
                min =i
            profit = i - min
            max_pro = max(max_pro,profit)
        return max_pro        
