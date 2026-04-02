class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Get the total number of points
        num_points = len(points)
      
        # Initialize the maximum count to 1 (at least one point exists)
        max_points_on_line = 1
      
        # Iterate through each point as the first reference point
        for i in range(num_points):
            x1, y1 = points[i]
          
            # Iterate through each subsequent point as the second reference point
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
              
                # Start with 2 points (the two reference points are always on the same line)
                points_on_current_line = 2
              
                # Check all remaining points to see if they're collinear with the two reference points
                for k in range(j + 1, num_points):
                    x3, y3 = points[k]
                  
                    # Check collinearity using cross product
                    # Points are collinear if (y2-y1)/(x2-x1) = (y3-y1)/(x3-x1)
                    # To avoid division, we cross-multiply: (y2-y1)*(x3-x1) = (y3-y1)*(x2-x1)
                    cross_product_left = (y2 - y1) * (x3 - x1)
                    cross_product_right = (y3 - y1) * (x2 - x1)
                  
                    # If the cross products are equal, the point is on the same line
                    if cross_product_left == cross_product_right:
                        points_on_current_line += 1
              
                # Update the maximum count if current line has more points
                max_points_on_line = max(max_points_on_line, points_on_current_line)
      
        return max_points_on_line