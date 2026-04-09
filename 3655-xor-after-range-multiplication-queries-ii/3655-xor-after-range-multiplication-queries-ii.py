from functools import reduce
from operator import xor
from math import sqrt
from collections import defaultdict
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        sq = int(sqrt(n))
        mp = defaultdict(list)

        # Process queries
        for l, r, k, v in queries:
            if k > sq:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                mp[k].append((l, r, v))

        # Process small k using difference array
        for k in mp:
            dif = [1] * (n + k)

            for l, r, v in mp[k]:
                dif[l] = (dif[l] * v) % MOD
                rplus1 = l + ((r - l) // k + 1) * k
                if rplus1 < len(dif):
                    dif[rplus1] = (dif[rplus1] * pow(v, -1, MOD)) % MOD

            # prefix multiplication
            for i in range(k, n):
                dif[i] = (dif[i] * dif[i - k]) % MOD

            # apply to nums
            for i in range(n):
                nums[i] = (nums[i] * dif[i]) % MOD

        # XOR result
        res = 0
        for x in nums:
            res ^= x

        return res