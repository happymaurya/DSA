class Solution {
    /**
     * Calculate the number of unique paths from top-left to bottom-right in an m x n grid.
     * Movement is restricted to either right or down at any point.
     * 
     * @param m number of rows in the grid
     * @param n number of columns in the grid
     * @return total number of unique paths
     */
    public int uniquePaths(int m, int n) {
        // Create a 2D DP array to store the number of paths to each cell
        int[][] dp = new int[m][n];
      
        // Initialize the starting position with 1 path (base case)
        dp[0][0] = 1;
      
        // Fill the DP table by iterating through each cell
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                // Add paths from the cell above (if exists)
                if (row > 0) {
                    dp[row][col] += dp[row - 1][col];
                }
              
                // Add paths from the cell to the left (if exists)
                if (col > 0) {
                    dp[row][col] += dp[row][col - 1];
                }
            }
        }
      
        // Return the number of paths to reach the bottom-right corner
        return dp[m - 1][n - 1];
    }
}