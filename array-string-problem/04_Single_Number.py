class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        k = len(nums)
        return Counter(nums).most_common(k)[-1][0]
