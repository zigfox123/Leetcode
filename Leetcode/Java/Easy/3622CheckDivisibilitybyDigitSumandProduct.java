class Solution{
    public boolean checkDivisibility(int n){
        if(n == 0){
            return false;
        }
        int product = 1;
        int sum = 0;
        String string_n = Integer.toString(n);
        for(int i =0; i < string_n.length(); i++){
            
            sum += Integer.valueOf(string_n.charAt(i) - '0');
            product *= Integer.valueOf(string_n.charAt(i) - '0');
        }
        int total_sum = sum + product;
        if(n % total_sum == 0){
            return true;
        }else{
            return false;
        }
    }
}
//Accepted solution