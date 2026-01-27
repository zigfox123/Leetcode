import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int romanToInt(String s) {
         int output = 0;
    int alreadyDone = 0;
    List<Integer> outputList = new ArrayList<>();
    
    Map<Character, Integer> valuesDict = new HashMap<>();
    valuesDict.put('I', 1);
    valuesDict.put('V', 5);
    valuesDict.put('X', 10);
    valuesDict.put('L', 50);
    valuesDict.put('C', 100);
    valuesDict.put('D', 500);
    valuesDict.put('M', 1000);
    
    // Convert string to list of values
    for (char c : s.toCharArray()) {
        outputList.add(valuesDict.get(c));
    }
    
    // Calculate the integer value
    for (int i = 0; i < outputList.size(); i++) {
        if (alreadyDone == 1) {
            alreadyDone = 0;
        } else if (i == outputList.size() - 1) {
            output += outputList.get(i);
        } else if (outputList.get(i) >= outputList.get(i + 1)) {
            output += outputList.get(i);
        } else {
            output += outputList.get(i + 1) - outputList.get(i);
            alreadyDone = 1;
        }
    }
    
    return output;
        
        
    }
}