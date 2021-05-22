class Solution {
    public void moveZeroes(int[] nums) {
        //[0,1,0,3,12]
        int i = 0;
        int j = 1;
        int n = nums.length;
        while(j<n) {
            if(nums[i] == 0 && nums[j] != 0) {
                int t = nums[i];
                nums[i] = nums[j];
                nums[j] = t;
                
                i++;
                j++;
            } else if(nums[i] == 0 && nums[j] == 0) {
                j++;
            } 
            else {
                i++;
                j++;
            }
        }
    }
}