class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Dictionary to store the last index of each character in the string
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set() # To keep track of characters currently in the stack
        
        for i, char in enumerate(s):
            # If the character is already in our stack, we don't need to add it again
            if char in seen:
                continue
            
            # Pop elements from the stack if:
            # 1. The stack is not empty
            # 2. The current character is smaller than the top of the stack
            # 3. The character at the top of the stack appears again later in the string
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)