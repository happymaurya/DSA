from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Count characters to form the first half
        counts = Counter(s)
        mid_char = ""
        half_counts = [0] * 26
        
        for char, count in counts.items():
            if count % 2 != 0:
                mid_char = char
            half_counts[ord(char) - ord('a')] = count // 2
            
        total_half_len = sum(half_counts)
        
        # Helper function to count permutations safely capped at k
        def count_perms_capped(counts, k):
            total = sum(counts)
            ans = 1
            for c in counts:
                if c <= 0: 
                    continue
                comp = 1
                r = min(c, total - c)
                for i in range(1, r + 1):
                    comp = comp * (total - i + 1) // i
                    if ans * comp >= k:
                        return k
                ans *= comp
                total -= c
                if ans >= k:
                    return k
            return ans

        # If the total possible permutations are less than k, return empty string
        if count_perms_capped(half_counts, k) < k:
            return ""
            
        first_half = []
        # Build the first half character by character
        for _ in range(total_half_len):
            for i in range(26):
                if half_counts[i] > 0:
                    # Tentatively place character i
                    half_counts[i] -= 1
                    perms = count_perms_capped(half_counts, k)
                    
                    if perms >= k:
                        # Character i is the correct choice for this position
                        first_half.append(chr(ord('a') + i))
                        break
                    else:
                        # Skip all permutations starting with character i
                        k -= perms
                        half_counts[i] += 1
                        
        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]
