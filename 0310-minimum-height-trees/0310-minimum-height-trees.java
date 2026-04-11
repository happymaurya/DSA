import java.util.*;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // Edge case
        if (n == 1) {
            return Collections.singletonList(0);
        }

        // Step 1: Build graph
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        int[] degree = new int[n];

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            graph.get(u).add(v);
            graph.get(v).add(u);

            degree[u]++;
            degree[v]++;
        }

        // Step 2: Add initial leaves
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) {
                queue.offer(i);
            }
        }

        int remainingNodes = n;

        // Step 3: Remove leaves layer by layer
        while (remainingNodes > 2) {
            int size = queue.size();
            remainingNodes -= size;

            for (int i = 0; i < size; i++) {
                int leaf = queue.poll();

                for (int neighbor : graph.get(leaf)) {
                    degree[neighbor]--;

                    if (degree[neighbor] == 1) {
                        queue.offer(neighbor);
                    }
                }
            }
        }

        // Remaining nodes are centroids
        return new ArrayList<>(queue);
    }
}