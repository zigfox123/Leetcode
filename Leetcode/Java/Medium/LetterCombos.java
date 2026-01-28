//Accepted answer for Leetcode problem 17 "Letter Combinations of a Phone Number"
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution{
    public List<String> letterCombinations(String digits) {
        if (digits.length() ==0){
            return new ArrayList<String>();
        }
        Map<Integer, String> dict = new HashMap<>();
        dict.put(2, "abc");
        dict.put(3, "def");
        dict.put(4, "ghi");
        dict.put(5, "jkl");
        dict.put(6, "mno");
        dict.put(7, "pqrs");
        dict.put(8, "tuv");
        dict.put(9, "wxyz");
        List<String> Output = new ArrayList<>();
        int holder = 0;
        while (holder < digits.length()){
            int current_digit = Character.getNumericValue(digits.charAt(holder));
            String letters = dict.get(current_digit);
            if (holder == 0) {
                for (int i = 0; i < letters.length(); i ++) {
                    Output.add(String.valueOf(letters.charAt(i)));
                }
            } else {
                List<String> temp = new ArrayList<>();
                for (String combo : Output) {
                    for (int i =0; i < letters.length(); i ++){
                        temp.add(combo + letters.charAt(i));
                    }
                }
                Output = temp;
            }
            holder += 1;

        }
        return Output;
        
    }
}