class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        std::vector<int> freq(26,0);
        for(char c:p){
            freq[c - 'a']++;
        }
        std::vector<int> indices;
        std::vector<int> o_freq(26,0);
        o_freq[s[0]-'a']++;
        if(o_freq == freq){
            indices.push_back(0);
        }
        int left = 0;
        int right = 0;
        while(right < (s.size()-1)){
            if((right - left + 1) < p.size()){
                right++;
                o_freq[s[right]-'a'] ++;
            }else{
                o_freq[s[left] - 'a'] --;
                left ++;
                right ++;
                o_freq[s[right] - 'a']++;
            }
            if(o_freq == freq){
                indices.push_back(left);
            }

        }
        return indices;
    }
};