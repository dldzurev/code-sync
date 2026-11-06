class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int left= 0;
        int right = 1;
        int curr_max = 0;
        int curr_sum = 0;
        while(right < prices.size()){
            if(prices[right] < prices[left]){
                left = right;     
            }
            if((prices[right] - prices[left]) > curr_max){
                curr_max = prices[right] - prices[left];
            }
            right ++;
        }
        return curr_max;
    }
};