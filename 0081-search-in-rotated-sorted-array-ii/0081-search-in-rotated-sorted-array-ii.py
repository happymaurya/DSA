class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Search for target in a rotated sorted array that may contain duplicates.
        Uses modified binary search to handle rotation and duplicates.

        Args:
            nums: Rotated sorted array possibly with duplicates
            target: Value to search for

        Returns:
            True if target exists in array, False otherwise
        """
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            # Calculate middle index
            mid = (left + right) // 2

            # Case 1: Left half is sorted (mid value > right value)
            if nums[mid] > nums[right]:
                # Check if target is in the sorted left half
                if nums[left] <= target <= nums[mid]:
                    # Target is in left half, search there
                    right = mid
                else:
                    # Target must be in right half
                    left = mid + 1

            # Case 2: Right half is sorted (mid value < right value)
            elif nums[mid] < nums[right]:
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    # Target is in right half, search there
                    left = mid + 1
                else:
                    # Target must be in left half
                    right = mid

            # Case 3: Cannot determine which half is sorted due to duplicates
            # (nums[mid] == nums[right])
            else:
                # Reduce search space by moving right pointer
                right -= 1

        # Check if the remaining element is the target
        return nums[left] == target
