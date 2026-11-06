class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        std::sort(events.begin(),events.end());
        std::priority_queue<int,std::vector<int>,std::greater<int>> minheap;
        int i = 0;
        int day = 0;
        int count = 0;
        int n = events.size();

        while(i < n || !minheap.empty()){
            if (minheap.empty()){//skip days with no events
                day = events[i][0];
            }
            //add events that have started
            while(i<n && events[i][0]<=day){
                minheap.push(events[i][1]);//push end date
                i++;
            }
            //remove expired events
            while(!minheap.empty() && minheap.top()<day){
                minheap.pop();
            }
            //attend earliest ending event
            if(!minheap.empty()){
                minheap.pop();
                count++;
            }
            day++;
        }
        return count;
    }
};