class Solution{
    public:
        bool checkDivisibility(int n){
            int product =1;
            int sum = 0;
            string string_n = to_string(n);
            for(int i = 0; i < string_n.length(); i++){
                int digit = string_n[i] - '0';
                sum += digit;
                product *= digit;
            }
            int total_sum = sum + product;
            if(n % total_sum == 0){
                return true;
            }else{
                return false;
            }
        }
};
//Accepted solution