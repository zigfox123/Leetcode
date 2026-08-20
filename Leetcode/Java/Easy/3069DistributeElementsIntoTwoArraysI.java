import java.util.ArrayList;

class Solution{
    public int[] resultArray(int[] nums){
        ArrayList<Integer> arr1 = new ArrayList<>();
        ArrayList<Integer> arr2 = new ArrayList<>();
        int result[] = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            if(i == 0){
                arr1.add(nums[i]);
            }else if(i == 1){
                arr2.add(nums[i]);
            }
            else if(arr1.get(arr1.size() - 1) > arr2.get(arr2.size() -1)){
                arr1.add(nums[i]);
            }else{
                arr2.add(nums[i]);
            }
        
        for(int j = 0; j < arr1.size(); j++){
            result[j] = arr1.get(j);
        }
        for(int k = 0; k < arr2.size(); k++){
            result[arr1.size() + k] = arr2.get(k);
        }
        }
    return result;
        
    }
}
//Accepted solution