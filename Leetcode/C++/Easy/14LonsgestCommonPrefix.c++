#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
    string longestCommonPrefix(vector<string>& strs) {
        //Find the longest common prefix for all the strings
        string first_words = strs[0];
        for( int i = 0; i < strs.size(); i++){
            while(strs[i].find(first_words) != 0){
                first_words = first_words.substr(0, first_words.size() - 1);
                if (first_words.empty()){
                    return "";
                }
            }
        }

        return first_words;
    }
};
//Accepted Solution