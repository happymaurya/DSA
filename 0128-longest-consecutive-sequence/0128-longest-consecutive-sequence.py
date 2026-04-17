class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set for O(1) lookup of numbers
        remaining_numbers = set(nums)

        # Initialize the maximum sequence length
        max_length = 0

        # Dictionary to cache the length of sequences starting from each number
        sequence_lengths = {}

        # Process each number in the original array
        for current_num in nums:
            # Skip if this number was already processed as part of another sequence
            if current_num not in remaining_numbers:
                continue

            # Find the end of the consecutive sequence starting from current_num
            sequence_end = current_num
            while sequence_end in remaining_numbers:
                # Remove processed numbers to avoid reprocessing
                remaining_numbers.remove(sequence_end)
                sequence_end += 1

            # Calculate the length of the sequence from current_num to sequence_end-1
            # If sequence_end is already in the dictionary, we can reuse its cached length
            current_length = (sequence_end - current_num) + sequence_lengths.get(sequence_end, 0)
            sequence_lengths[current_num] = current_length

            # Update the maximum length found so far
            max_length = max(max_length, current_length)

        return max_length