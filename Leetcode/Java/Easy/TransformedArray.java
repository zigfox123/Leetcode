//Accepted answer for leetcode problem 3379 Transformed Array

class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int[] result = new int[nums.length];

        for (int i = 0; i <nums.length; i++){
            int n = nums[i];
            if (i + n < nums.length && i + n >= 0){
                result[i] += nums[i +n];
            } else if (i + n >=nums.length){
               int overflow = (i + n) / nums.length;
               int overflow_result = (i + n) -(overflow * nums.length);
               result[i] += nums[overflow_result];
            }else{
                int underflow = (i +n) / nums.length;
                int underflow_result = (i + n) - (underflow * nums.length);
                if (underflow_result < 0){
                    underflow_result += nums.length;
                    result[i] += nums[underflow_result];
                }else{
                result[i] += nums[underflow_result];
            }
        }        
        }
    return result;
    }
}