class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        // Edge cases
        if ((target + totalSum) % 2 != 0 || Math.abs(target) > totalSum) {
            return 0;
        }

        int P = (target + totalSum) / 2;

        // DP array
        int[] dp = new int[P + 1];
        dp[0] = 1; // one way to make sum 0

        for (int num : nums) {
            for (int j = P; j >= num; j--) {
                dp[j] += dp[j - num];
            }
        }

        return dp[P];
    }
}