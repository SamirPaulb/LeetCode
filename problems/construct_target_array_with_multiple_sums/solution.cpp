    class Solution {
    public:
        bool isPossible(vector<int>& target) {
            if(target.size()==0) return true;
            if(target.size()==1 ){
                if(target[0]==1) return true;
                else return false;
            }
            priority_queue<int> record;
            long sum = 0;
            for(int i=0; i<target.size(); ++i){
                record.push(target[i]);
                sum += target[i];
            }
            while(sum>target.size()){
                int iter = record.top();
                record.pop();
                if(iter == 1) return true;
                if(iter > sum - iter){
                    if(record.top() == 1) return true;
                    int tmp = sum - iter;
                    int sub = iter / tmp;
                    int num = iter % tmp;
                    if(num == 0) return false;
                    record.push(num);
                    sum -= tmp * sub;
                }else return false;
            }
            return true;
        }
    };