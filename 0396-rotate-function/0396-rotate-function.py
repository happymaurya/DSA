class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Find the maximum value of rotation function F(k) for all k from 0 to n-1.
        F(k) = 0*arr[k] + 1*arr[k+1] + ... + (n-1)*arr[k+n-1]
        where arr[i] represents the rotated array.
        """
        current_rotation_value = sum(index * value for index, value in enumerate(nums))
      
        array_length = len(nums)
        total_sum = sum(nums)
      
        # Initialize maximum with F(0)
        max_rotation_value = current_rotation_value
      
        for rotation in range(1, array_length):
           
            current_rotation_value = current_rotation_value + total_sum - array_length * nums[array_length - rotation]
          
            
            max_rotation_value = max(max_rotation_value, current_rotation_value)
      
        return max_rotation_value