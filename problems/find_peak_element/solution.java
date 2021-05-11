public class Solution {
    public int findPeakElement(int[] num) {
        int max = num[0];
        int index = 0;
        for(int i=1; i<=num.length-2; i++){
            int prev = num[i-1];
            int curr = num[i];
            int next = num[i+1];
 
            if(curr > prev && curr > next && curr > max){
                index = i;
                max = curr;
            }
        }
 
        if(num[num.length-1] > max){
            return num.length-1;
        }
 
        return index;
    }
}