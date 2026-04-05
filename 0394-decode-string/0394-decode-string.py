class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        
        current_string = ""
        k = 0
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # handle multi-digit numbers
            
            elif char == '[':
                count_stack.append(k)
                string_stack.append(current_string)
                k = 0
                current_string = ""
            
            elif char == ']':
                repeat_times = count_stack.pop()
                prev_string = string_stack.pop()
                current_string = prev_string + current_string * repeat_times
            
            else:
                current_string += char
        
        return current_string