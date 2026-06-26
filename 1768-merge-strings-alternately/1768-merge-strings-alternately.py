class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        merged=""
        while left<len(word1) or left<len(word2):
            if left<len(word1):
                merged+=word1[left]
            if left<len(word2):
                merged+=word2[left]
            left+=1
        return merged

