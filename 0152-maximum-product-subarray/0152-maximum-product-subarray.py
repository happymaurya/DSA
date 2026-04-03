class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize: max_product tracks the overall maximum product found
        # max_ending_here tracks the maximum product ending at current position
        # min_ending_here tracks the minimum product ending at current position
        max_product = max_ending_here = min_ending_here = nums[0]
      
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Store previous values before updating
            prev_max = max_ending_here
            prev_min = min_ending_here
          
            # Update max_ending_here: it could be:
            # 1. The current number itself (starting fresh)
            # 2. Previous max times current (if both positive or both negative)
            # 3. Previous min times current (if one is negative, could flip to max)
            max_ending_here = max(num, prev_max * num, prev_min * num)
          
            # Update min_ending_here: similar logic but taking minimum
            # We track minimum because a negative number could flip it to maximum later
            min_ending_here = min(num, prev_max * num, prev_min * num)
          
            # Update the overall maximum product found so far
            max_product = max(max_product, max_ending_here)
      
        return max_product
