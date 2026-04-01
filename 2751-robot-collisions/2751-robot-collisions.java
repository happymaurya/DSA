class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }

        Arrays.sort(indices, (i, j) -> Integer.compare(positions[i], positions[j]));
      
        Stack<Integer> stack = new Stack<>();
      
        // Process robots from left to right based on their positions
        for (int currentIndex : indices) {
            if (directions.charAt(currentIndex) == 'R') {
                // Robot moving right: add to stack (potential collision candidate)
                stack.push(currentIndex);
            } else {
                // Robot moving left: check for collisions with robots moving right
                while (!stack.isEmpty() && healths[currentIndex] > 0) {
                    int rightMovingRobotIndex = stack.pop();
                  
                    if (healths[rightMovingRobotIndex] > healths[currentIndex]) {
                        // Right-moving robot wins: decrease its health by 1
                        healths[rightMovingRobotIndex] -= 1;
                        healths[currentIndex] = 0;
                        stack.push(rightMovingRobotIndex); // Put winner back on stack
                    } else if (healths[rightMovingRobotIndex] < healths[currentIndex]) {
                        // Left-moving robot wins: decrease its health by 1
                        healths[currentIndex] -= 1;
                        healths[rightMovingRobotIndex] = 0;
                        // Continue checking for more collisions
                    } else {
                        // Both robots have equal health: both are destroyed
                        healths[currentIndex] = 0;
                        healths[rightMovingRobotIndex] = 0;
                    }
                }
            }
        }
      
        List<Integer> result = new ArrayList<>();
        for (int health : healths) {
            if (health > 0) {
                result.add(health);
            }
        }
      
        return result;
    }
}