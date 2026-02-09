class Solution {
    public int minimumPairRemoval(int[] nums) {
        int output = 0;
        
        if (nums.length == 0){
            return 0;
        }
        //check if the array is already sorted
        int check_already_sorted = 0;
        for(int i = 0; i < nums.length; i++ ){
            if(nums[i] < nums[i + 1]){
                check_already_sorted += 1;
            }
        }
        if (check_already_sorted == nums.length){
            return 0;
        }

        
    }
}