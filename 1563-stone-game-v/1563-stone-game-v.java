class Solution {
    private int[][] memo;
    private int[] prefixSums;

    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        memo = new int[n][n];
        prefixSums = new int[n + 1];
        
        // Precompute prefix sums for O(1) range sum queries
        for (int i = 0; i < n; i++) {
            prefixSums[i + 1] = prefixSums[i] + stoneValue[i];
        }
        
        return solve(0, n - 1);
    }

    private int solve(int i, int j) {
        // Base case: only one stone left, no further score can be obtained
        if (i == j) {
            return 0;
        }
        
        // Return cached result if already calculated
        if (memo[i][j] != 0) {
            return memo[i][j];
        }

        int maxScore = 0;

        // Try every possible split point k between i and j
        for (int k = i; k < j; k++) {
            int leftSum = prefixSums[k + 1] - prefixSums[i];
            int rightSum = prefixSums[j + 1] - prefixSums[k + 1];

            if (leftSum < rightSum) {
                // Bob throws away the right row; Alice keeps the left row
                maxScore = Math.max(maxScore, leftSum + solve(i, k));
            } else if (leftSum > rightSum) {
                // Bob throws away the left row; Alice keeps the right row
                maxScore = Math.max(maxScore, rightSum + solve(k + 1, j));
            } else {
                // Sums are equal; Alice chooses the choice maximizing her score
                int chooseLeft = leftSum + solve(i, k);
                int chooseRight = rightSum + solve(k + 1, j);
                maxScore = Math.max(maxScore, Math.max(chooseLeft, chooseRight));
            }
        }

        return memo[i][j] = maxScore;
    }
}
