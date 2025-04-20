class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """BruteForce:
        Generate all permutations of the words in the words list.
        Concatenate each permutation into a string.
        Search the entire string s for substrings that match any of the permutations.
        it can be as bad as. O(nK!) where n is len s and k is len words"""
        """Smart Sliding Window + HashMap Solution"""
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result=[]

        for i in range(word_len):
            left = i
            curr_count = Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    curr_count[word] += 1
                    # shrink window from the left if word count exceeds
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        curr_count[left_word] -= 1
                        left += word_len

                    # if window matches total length, record the start index
                    if j + word_len - left == total_len:
                        result.append(left)
                else:
                    # reset window
                    curr_count.clear()
                    left = j + word_len

        return result