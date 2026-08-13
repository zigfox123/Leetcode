class Solution{
    public int maxProfit(int[] prices){
        int max_amount = 0;
        int min_price = prices[0];
        for (int i = 0; i < prices.length; i++){
            min_price = Math.min(min_price, prices[i]);
            max_amount = Math.max(max_amount, prices[i] - min_price);

            
        }
        return max_amount;
    }
}

//Accepted solution