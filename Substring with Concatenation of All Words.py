from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for i in range(word_len):  # Try every offset
            left = i
            window_counter = Counter()
            count = 0  # number of valid words in current window

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_freq:
                    window_counter[word] += 1
                    count += 1

                    # If we have too many of one word, slide window
                    while window_counter[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        window_counter[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)
                else:
                    window_counter.clear()
                    count = 0
                    left = j + word_len

        return result
