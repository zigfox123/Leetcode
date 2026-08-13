class Solution{
    public boolean isPalindrome(String s){
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        String reversed_s = "";
        for(int i = 0; i < s.length(); i++){
            reversed_s = s.charAt(i) + reversed_s;
        }

        if (reversed_s.equals(s)){
            return true;
        }else{
            return false;
        }

    }
}
//Accepted answer