class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        # Calculate area of rectangle A
        # Rectangle A has bottom-left corner (ax1, ay1) and top-right corner (ax2, ay2)
        area_rectangle_a = (ax2 - ax1) * (ay2 - ay1)
      
        # Calculate area of rectangle B
        # Rectangle B has bottom-left corner (bx1, by1) and top-right corner (bx2, by2)
        area_rectangle_b = (bx2 - bx1) * (by2 - by1)
      
        # Calculate the overlap dimensions between the two rectangles
        # For overlap to exist, the rectangles must intersect both horizontally and vertically
      
        # Find the width of the overlapping region
        # The overlap starts at the rightmost left edge and ends at the leftmost right edge
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
      
        # Find the height of the overlapping region
        # The overlap starts at the topmost bottom edge and ends at the bottommost top edge
        overlap_height = min(ay2, by2) - max(ay1, by1)
      
        # Calculate the overlapping area
        # If either dimension is negative, there's no overlap, so we use max with 0
        overlap_area = max(overlap_height, 0) * max(overlap_width, 0)
      
        # Total area = Area of A + Area of B - Overlapping area
        # We subtract the overlap to avoid counting it twice
        return area_rectangle_a + area_rectangle_b - overlap_area
