class Solution {
    public boolean isPalindrome(int x) {
        String strX = Integer.toString(x);
        String reversedX = "";
        for (int i = 0; i < strX.length(); i++){
            reversedX = strX.charAt(i) + reversedX;
        }
        if (reversedX.equals(strX)){
            return true;
        }else{
            return false;
        }
    }
}

//Accepted Solution