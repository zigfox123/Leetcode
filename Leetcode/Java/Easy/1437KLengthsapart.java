class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        if (k == 0){
            return(true);
        }
        for (int i = 1; i < nums.length; i++) {

            if (nums[i] == 1) {
                for (int j = 1; j < nums.length; j++){
                    if (nums[j]== 1 && (j > i) && ((j - i -1) < k)){
                        return(false);
                    }
                }
            } 

        }
        return(true);
}
}
//Not done yet