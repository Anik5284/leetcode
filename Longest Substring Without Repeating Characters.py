class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Stores the most recent index of each character
        left = 0         # Left pointer of the window
        max_len = 0      # Max length found so far

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # If the character is repeated, move the left pointer
                left = char_index[s[right]] + 1
            # Update the latest index of the character
            char_index[s[right]] = right
            # Calculate the max length of current window
            max_len = max(max_len, right - left + 1)

        return max_len
