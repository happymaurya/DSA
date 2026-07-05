class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int n = board.size(), M = 1e9 + 7;
        vector<vector<int>> score(n, vector<int>(n)), path = score;
        vector<vector<int>> dirs{{0, -1}, {-1, 0}, {-1, -1}};
        path[n - 1][n - 1] = 1;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (path[i][j] == 0) continue;
                for (auto dir : dirs) {
                    int x = i + dir[0], y = j + dir[1];
                    if (x < 0 || y < 0 || board[x][y] == 'X') continue;
                    int sum = score[i][j];
                    if (board[x][y] != 'E') sum += board[x][y] - '0';
                    if (sum > score[x][y]) {
                        score[x][y] = sum;
                        path[x][y] = path[i][j];
                    } else if (sum == score[x][y]) {
                        path[x][y] = (path[x][y] + path[i][j]) % M;
                    }
                }
            }
        }
        return {score[0][0], path[0][0]};
    }
};