class Solution {
    
    public int numOfStrings(String[] patterns, String word) {
   
        int matchCount = 0;
      
        for (String pattern : patterns) {
            if (word.contains(pattern)) {
               
                matchCount++;
            }
        }
      
        // Return the total count of matching patterns
        return matchCount;
    }
}