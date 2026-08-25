class Solution{
    public int missingMultiple(int[] nums, int k){
        boolean ans_found = false;
        boolean found = false;
        int multiple = 1;
        int ans;
        
        while(ans_found == false){
            ans = multiple * k;
            found = false;
            for(int num : nums){
                if(num == ans){
                    found = true;
                    break;
                }
            }
            if(found == false){
                return ans;
            }
            multiple += 1;
        }
        return 0;
    }
}
//Accepted answer