import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // Step 1: Create graph
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        // Step 2: Indegree array
        int[] indegree = new int[numCourses];

        // Step 3: Fill graph and indegree
        for (int[] pre : prerequisites) {
            int course = pre[0];
            int prereq = pre[1];
            graph.get(prereq).add(course);
            indegree[course]++;
        }

        // Step 4: Queue for BFS
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // Step 5: Process queue
        int[] result = new int[numCourses];
        int index = 0;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            result[index++] = current;

            for (int neighbor : graph.get(current)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // Step 6: Check if all courses are completed
        if (index == numCourses) {
            return result;
        }

        // Cycle detected
        return new int[0];
    }
}