class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Step 2: Extract the characters for the first half and find the middle character (if any)
        half_chars = []
        mid_char = ""
        
        for char, count in char_counts.items():
            # If a character has an odd count, one instance goes to the middle
            if count % 2 == 1:
                mid_char = char
            # Half of the total count of this character forms the left side
            half_chars.extend([char] * (count // 2))
        
        # Step 3: Sort the first half to make it lexicographically smallest
        half_chars.sort()
        
        # Step 4: Reconstruct the full string
        left_half = "".join(half_chars)
        right_half = left_half[::-1]
        
        return left_half + mid_char + right_half
