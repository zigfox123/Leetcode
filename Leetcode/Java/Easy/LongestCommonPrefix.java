
class Solution {
    public String longestCommonPrefix(String[] strs) {
      String first_word =  strs[0];//Gets the first word
        for (int i = 1; i < strs.length; i++) {
            String s = strs[i];
            while (!s.startsWith(first_word)){
                first_word = first_word.substring(0, first_word.length() - 1);
                if (first_word.isEmpty())
                    return "";
            }
        }
        return first_word;
    }
}
//Accepted answer