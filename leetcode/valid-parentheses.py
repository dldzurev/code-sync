class Solution {
public:
    bool isValid(string s) {
        // if we hit a close we need a the samme open
        std::unordered_map<char,char> map;
        map['}'] = '{';
        map[']'] = '[';
        map[')'] = '(';
        std::stack<char> my_stack;
        for(char b :s){
            if(map.count(b)){
                if(my_stack.empty() || !(my_stack.top() == map[b])){
                    return false;
                }
                my_stack.pop();
            }else{
                my_stack.push(b);
            }
        }
        if(my_stack.size() > 0){
            return false;
        }else{
            return true;
        }
    }
};