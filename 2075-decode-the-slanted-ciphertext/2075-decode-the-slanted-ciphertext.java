class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        if (rows == 1) return encodedText;

        int n = encodedText.length();
        int cols = n / rows;

        StringBuilder result = new StringBuilder();

        for (int c = 0; c < cols; c++) {
            int i = 0, j = c;

            while (i < rows && j < cols) {
                result.append(encodedText.charAt(i * cols + j));
                i++;
                j++;
            }
        }

        // remove trailing spaces
        int end = result.length();
        while (end > 0 && result.charAt(end - 1) == ' ') {
            end--;
        }

        return result.substring(0, end);
    }
}