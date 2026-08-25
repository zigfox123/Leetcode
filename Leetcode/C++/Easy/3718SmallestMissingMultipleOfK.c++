class Solution{
    public:
        int missingMultiple(vector<int>& nums, int k){
            bool ans_found = false;
            int multiple = 1;
            int ans;
            while(!ans_found){
                ans  = multiple * k;
                if(find(nums.begin(), nums.end(), ans) == nums.end()){
                    return ans;
                    
                }
                multiple += 1;
            }
            return 0;
        }
};
//Accepted solution