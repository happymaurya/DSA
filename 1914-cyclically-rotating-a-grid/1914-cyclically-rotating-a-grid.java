class Solution {
    private int rows;
    private int cols;
    private int[][] matrix;

    public int[][] rotateGrid(int[][] grid, int k) {
        rows = grid.length;
        cols = grid[0].length;
        this.matrix = grid;
      
        int numLayers = Math.min(rows, cols) / 2;
      
        for (int layer = 0; layer < numLayers; ++layer) {
            rotateLayer(layer, k);
        }
      
        return grid;
    }

    private void rotateLayer(int layer, int k) {
        List<Integer> elements = new ArrayList<>();
      
        for (int col = layer; col < cols - layer - 1; ++col) {
            elements.add(matrix[layer][col]);
        }
      
        for (int row = layer; row < rows - layer - 1; ++row) {
            elements.add(matrix[row][cols - layer - 1]);
        }
      
        for (int col = cols - layer - 1; col > layer; --col) {
            elements.add(matrix[rows - layer - 1][col]);
        }
      
        for (int row = rows - layer - 1; row > layer; --row) {
            elements.add(matrix[row][layer]);
        }
      
       
        int layerSize = elements.size();
        k %= layerSize;
      
        if (k == 0) {
            return;
        }
      
        for (int col = layer; col < cols - layer - 1; ++col) {
            matrix[layer][col] = elements.get(k++ % layerSize);
        }
      
        for (int row = layer; row < rows - layer - 1; ++row) {
            matrix[row][cols - layer - 1] = elements.get(k++ % layerSize);
        }
      
        for (int col = cols - layer - 1; col > layer; --col) {
            matrix[rows - layer - 1][col] = elements.get(k++ % layerSize);
        }
      
        for (int row = rows - layer - 1; row > layer; --row) {
            matrix[row][layer] = elements.get(k++ % layerSize);
        }
    }
}
