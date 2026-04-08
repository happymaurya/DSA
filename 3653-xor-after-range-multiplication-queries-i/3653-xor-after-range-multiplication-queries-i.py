from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Process each query
        for l, r, k, v in queries:
            # Apply the operation: update indices l, l+k, l+2k... up to r
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        
        # Calculate the final XOR sum of the array
        result = 0
        for num in nums:
            result ^= num
            
        return result