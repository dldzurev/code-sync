class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> seen;
        int i = 0;
        for(int num:nums){
            int need = target - num;
            if(seen.count(need)){
                std::vector<int> ret = {i,seen[need]}; 
                return ret;
            }
            seen[num] = i;
            i++;
        }
        return {};
    }
    
};