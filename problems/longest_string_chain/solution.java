
class Solution {
    public int longestStrChain(String[] words) {
        Map<String,Integer> dp = new HashMap<>();
        Arrays.sort(words,(a,b)->a.length()-b.length());
        int result=0;
        for(String word:words)
        {
            int max=0;
            for(int i=0;i<word.length();i++)
            {
                String prev=word.substring(0,i)+word.substring(i+1);
                max=Math.max(max,dp.getOrDefault(prev,0)+1);
            }
            dp.put(word,max);
            result=Math.max(result,max);
        }
        return result;
    }
}