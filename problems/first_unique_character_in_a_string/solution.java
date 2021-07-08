class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> map = new LinkedHashMap<>();
        if(s == null) return -1;
        int n= s.length();
        for(int i=0; i<n; i++) {
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0)+1);
        }
        System.out.println(map);
        char uniChar = ' ';
        for(Map.Entry<Character, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 1) {
                uniChar = entry.getKey();
                break;
            }
        }
        
        if(uniChar == ' ') return -1;
        for(int i=0; i<n; i++) {
            char ch = s.charAt(i);
            if(ch == uniChar) return i;
        }
        return -1;
    }
}