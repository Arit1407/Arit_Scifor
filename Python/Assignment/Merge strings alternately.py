"""
Question :-
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        m=len(word1)
        n=len(word2)
        for i in range(min(m,n)):
             ans+=word1[i]+word2[i]
        if m>n:
            ans+=word1[n:]
        else:
            ans+=word2[m:]
        return ans
