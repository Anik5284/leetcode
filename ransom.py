class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        str1 = Counter(ransomNote)
        str2 = Counter(magazine)

        for char in str1:
            if str1[char] > str2.get(char, 0):
                return False
        return True
