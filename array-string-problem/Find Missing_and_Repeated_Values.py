class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        from collections import Counter
        n = len(grid)
        total = (n * n * (n * n + 1)) // 2  
        
        flat = [j for row in grid for j in row]  
        actual_sum = sum(flat)
        
        count = Counter(flat)
        repeated = [num for num, freq in count.items() if freq == 2][0]
        
        missing = total - (actual_sum - repeated)
        
        return [repeated, missing]
