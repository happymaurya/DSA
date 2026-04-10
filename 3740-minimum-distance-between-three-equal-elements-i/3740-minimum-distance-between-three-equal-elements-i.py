from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        mp = defaultdict(list)

        # Step 1: store indices
        for i, num in enumerate(nums):
            mp[num].append(i)

        ans = float('inf')

        # Step 2: process each value
        for indices in mp.values():
            if len(indices) >= 3:
                # Step 3: check consecutive triples
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i + 2] - indices[i])
                    ans = min(ans, dist)

        return ans if ans != float('inf') else -1