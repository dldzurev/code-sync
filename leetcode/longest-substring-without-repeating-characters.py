class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> curr_window;
        int left=0;
        int right=1;
        int max=1;
        if(s.size() == 0){
            return false;
        }
        curr_window.insert(s[0]);
        while(right < s.size()){
            
            while(curr_window.count(s[right])){
                curr_window.erase(s[left]);
                left++;
            }
            curr_window.insert(s[right]);
            if((right-left+1) > max){
                max = right-left+1;
            }
            right ++;
        }
        return max;
    }
};