class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int max = Integer.MIN_VALUE, sum = 0, i=0,j=0, s=0,e=0, l = nums.length;
        while(i<l && j<l) {
            while(j<l && !set.contains(nums[j])) {
                set.add(nums[j]);
                sum = sum+nums[j];
                if(max<sum) {
                    max = sum;
                    s = i;
                    e = j;
                }
                j++;
            }
            
            while(i<=j && i<l && j<l && set.contains(nums[j])) {
                set.remove(nums[i]);
                sum = sum - nums[i];
                if(max<sum) {
                    max = sum;
                    s = i;
                    e =j;
                }
                i++;
            }
        }
        System.out.println(s+" "+e);
        return max;
    }
}