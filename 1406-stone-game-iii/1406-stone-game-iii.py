class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)  # Extra padding to handle out-of-bounds easily
        
        # Traverse backwards from the end of the array
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp[i + 1]
            
            take2 = stoneValue[i] + (stoneValue[i + 1] if i + 1 < n else 0) - dp[i + 2]
            
            take3 = stoneValue[i] + (stoneValue[i + 1] if i + 1 < n else 0) + (stoneValue[i + 2] if i + 2 < n else 0) - dp[i + 3]
            
            dp[i] = max(take1, take2, take3)
            
        # Determine the winner based on Alice's relative score
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
