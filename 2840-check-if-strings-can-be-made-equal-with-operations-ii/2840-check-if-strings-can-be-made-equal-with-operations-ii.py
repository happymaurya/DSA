class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Check if two strings can be made equal by swapping characters at even indices
        with each other and odd indices with each other.
      
        Args:
            s1: First string to compare
            s2: Second string to compare
          
        Returns:
            True if strings can be made equal through allowed swaps, False otherwise
        """
        # Extract characters at even indices (0, 2, 4, ...) from both strings
        # and check if they contain the same characters (order doesn't matter)
        even_chars_match = sorted(s1[::2]) == sorted(s2[::2])
      
        # Extract characters at odd indices (1, 3, 5, ...) from both strings
        # and check if they contain the same characters (order doesn't matter)
        odd_chars_match = sorted(s1[1::2]) == sorted(s2[1::2])
      
        # Both even and odd position characters must match for the strings
        # to be transformable into each other
        return even_chars_match and odd_chars_match