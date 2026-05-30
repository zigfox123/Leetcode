#include <vector>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int k = nums.size();
        
        for(int i = 0; i< k; i++){
            for(int j = i+1; j < k; j++){
                if(nums[i]+ nums[j] == target){
                    
                    return {i,j};
                    
                   
                }

            }
        }
        return {};
        
    }
};

//Accepted answer