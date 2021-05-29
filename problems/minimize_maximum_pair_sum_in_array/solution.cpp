class Solution {
public:
    int minPairSum(vector<int>& nums) 
    {
        int n= nums.size();
        int i=0;
        int j=n-1;
        int ans=0;
        sort(nums.begin(),nums.end());
        while(i<n/2)
        {
            ans=max(ans,nums[i]+nums[j]);
            i++;
            j--;
        }
        return ans;
        
        
    }
};