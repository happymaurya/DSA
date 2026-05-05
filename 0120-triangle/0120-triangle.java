class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
    
        int triangleHeight = triangle.size();
      
        int[] minPathSum = new int[triangleHeight + 1];
      
        for (int row = triangleHeight - 1; row >= 0; row--) {
            
            for (int col = 0; col <= row; col++) {
              
                minPathSum[col] = Math.min(minPathSum[col], minPathSum[col + 1]) 
                                 + triangle.get(row).get(col);
            }
        }
      
        return minPathSum[0];
    }
}
