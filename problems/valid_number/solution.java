
class Solution {
    public boolean isNumber(String s) {
    s = s.trim();
    
    boolean pointPresent = false;
    boolean ePresent = false;
    boolean numberPresent = false;
    boolean numberAfterE = true;
    for(int i=0; i<s.length(); i++) {
        if('0' <= s.charAt(i) && s.charAt(i) <= '9') {
            numberPresent = true;
            numberAfterE = true;
        } else if(s.charAt(i) == '.') {
            if(ePresent || pointPresent) {
                return false;
            }
            pointPresent = true;
        } else if(s.charAt(i) == 'e' || s.charAt(i) =='E') {
            if(ePresent || !numberPresent) {
                return false;
            }
            numberAfterE = false;
            ePresent = true;
        } else if(s.charAt(i) == '-' || s.charAt(i) == '+') {
            if(i != 0 && s.charAt(i-1) != 'e') {
                return false;
            }
        } else {
            return false;
        }
    }
    
    return numberPresent && numberAfterE;
}
}