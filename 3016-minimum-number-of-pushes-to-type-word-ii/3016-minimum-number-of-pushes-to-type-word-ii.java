import java.util.Arrays;

class Solution {
    public int minimumPushes(String word) {
        int[] counts = new int[26];
        for (char c : word.toCharArray()) {
            counts[c - 'a']++;
        }
        
        Arrays.sort(counts);
        
        int totalPushes = 0;
        // Iterate backwards because Arrays.sort sorts in ascending order
        for (int i = 0; i < 26; i++) {
            int count = counts[25 - i];
            if (count == 0) break;
            
            int pushesNeeded = (i / 8) + 1;
            totalPushes += count * pushesNeeded;
        }
        
        return totalPushes;
    }
}
