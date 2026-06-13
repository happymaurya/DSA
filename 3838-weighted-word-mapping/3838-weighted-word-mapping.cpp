class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string ans = "";

        for (string s : words) {
            int val = 0;

            for (int i = 0; i < s.size(); i++) {
                val += weights[s[i] - 'a'];
            }

            val %= 26;

            char ch = 'z' - val;
            ans += ch;
        }

        return ans;
    }
};