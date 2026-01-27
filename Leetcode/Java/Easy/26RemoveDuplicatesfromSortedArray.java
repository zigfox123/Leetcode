import java.util.ArrayList;

class Solution {
    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> unique_numbers = new ArrayList<>();
        for(int i : nums){
            if (!unique_numbers.contains(i)) {
                unique_numbers.add(i);
            }
        }

        for(int i =0; i <unique_numbers.size(); i++){
            nums[i] = unique_numbers.get(i);
        }   

        return unique_numbers.size();

    }
}
//Accepted answer