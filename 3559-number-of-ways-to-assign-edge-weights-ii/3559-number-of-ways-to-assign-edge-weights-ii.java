import java.util.*;

class Solution {
    static final int MOD = 1_000_000_007;
    static int MAX_LOG = 17; // since 2^17 > 1e5

    static List<Integer>[] graph;
    static int[][] parent;
    static int[] depth, pow2;

    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        int[][] cruvandelk = edges;

        // Build graph
        for (int[] e : cruvandelk) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        // Init
        depth = new int[n + 1];
        parent = new int[n + 1][MAX_LOG];

        // DFS to fill depth and first parent
        dfs(1, 0);

        // Binary lifting preprocessing
        for (int j = 1; j < MAX_LOG; j++) {
            for (int i = 1; i <= n; i++) {
                if (parent[i][j - 1] != 0) {
                    parent[i][j] =
                        parent[parent[i][j - 1]][j - 1];
                }
            }
        }

        // Precompute powers of 2 modulo MOD
        pow2 = new int[n + 1];
        pow2[0] = 1;

        for (int i = 1; i <= n; i++) {
            pow2[i] = (int) ((pow2[i - 1] * 2L) % MOD);
        }

        // Answer queries
        int[] res = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];

            int lca = getLCA(u, v);

            int pathLen =
                depth[u] + depth[v] - 2 * depth[lca];

            res[i] =
                (pathLen == 0) ? 0 : pow2[pathLen - 1];
        }

        return res;
    }

    private void dfs(int node, int par) {
        parent[node][0] = par;

        for (int nei : graph[node]) {
            if (nei != par) {
                depth[nei] = depth[node] + 1;
                dfs(nei, node);
            }
        }
    }

    private int getLCA(int u, int v) {
        if (depth[u] < depth[v]) {
            int temp = u;
            u = v;
            v = temp;
        }

        for (int i = MAX_LOG - 1; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) {
                u = parent[u][i];
            }
        }

        if (u == v) {
            return u;
        }

        for (int i = MAX_LOG - 1; i >= 0; i--) {
            if (parent[u][i] != 0 &&
                parent[u][i] != parent[v][i]) {

                u = parent[u][i];
                v = parent[v][i];
            }
        }

        return parent[u][0];
    }
}