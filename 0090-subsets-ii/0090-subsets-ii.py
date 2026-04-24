class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            # Base case: if we've processed all elements
            if index == len(nums):
                result.append(current_subset[:])  # Add a copy of current subset
                return
          
            # Choice 1: Include the current element
            current_subset.append(nums[index])
            backtrack(index + 1)
          
            # Backtrack: remove the element we just added
            removed_element = current_subset.pop()
          
            # Skip all duplicates of the removed element
            # This ensures we don't create duplicate subsets
            while index + 1 < len(nums) and nums[index + 1] == removed_element:
                index += 1
          
            # Choice 2: Exclude the current element (and all its duplicates)
            backtrack(index + 1)
      
        # Sort the array to group duplicates together
        nums.sort()
      
        # Initialize result list and current subset being built
        result = []
        current_subset = []
      
        # Start the backtracking process from index 0
        backtrack(0)
      
        return result
