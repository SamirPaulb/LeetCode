class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n+1];
        dp[n] = true;
        for(int i=n-1; i>=0; i--) {
            for(String w : wordDict) {
                if(i+w.length() <= n 
                   && w.equals(s.substring(i, i+w.length()))) {
                    dp[i] = dp[i + w.length()];
                }
                if(dp[i]) break;
            }
        }
        return dp[0];
    }
}