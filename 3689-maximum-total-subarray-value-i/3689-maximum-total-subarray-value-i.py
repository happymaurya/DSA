class Solution:
    def maxTotalValue(self, nums, k):
        mx = nums[0]
        mn = nums[0]

        for x in nums:
            if x > mx:
                mx = x
            if x < mn:
                mn = x

        return (mx - mn) * k