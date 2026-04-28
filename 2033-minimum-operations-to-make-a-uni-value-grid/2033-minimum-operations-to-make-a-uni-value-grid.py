class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        flattened_values = []
      
       
        reference_remainder = grid[0][0] % x
      
        
        for row in grid:
            for value in row:
     
                if value % x != reference_remainder:
                    return -1
                flattened_values.append(value)
      
        flattened_values.sort()
      
        median_index = len(flattened_values) // 2
        median_value = flattened_values[median_index]
      
        total_operations = sum(abs(value - median_value) // x for value in flattened_values)
      
        return total_operations