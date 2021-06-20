class Solution {
public:
    string largestOddNumber(string num) {
        
        int len = num.length();
        
        for(int i = len-1; i>=0; i--)
        {
            if((num[i]-48)%2==0)
            {
                num.erase(i,1);
            }
            else{
                break;
            }
        }
        return num;
        
    }
};