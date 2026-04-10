class Solution:
    def singleNumber(self, nums):
        xor_all = 0
        
        # Step 1: XOR all numbers
        for num in nums:
            xor_all ^= num
        
        # Step 2: find rightmost set bit
        diff = xor_all & -xor_all
        
        # Step 3: divide into two groups
        a, b = 0, 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        
        return [a, b]