class Solution {
public:
    int numberOfSubstrings(string s) {
        int ans = 0;
        int left = 0;
        unordered_map<char, int> count;

        for (int right = 0; right <s.size(); right++) {
            count[s[right]]++;

            while (count['a'] > 0 && count['b'] > 0 && count['c'] > 0) {
                ans += s.size() -right;
                count[s[left]]--;
                left++;
            }
        }
        return ans;
    }
};

//Solution accepted runs in O(n) time using a sliding window approach.