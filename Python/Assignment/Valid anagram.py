"""
Question:-
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            count_s={}
            count_t={}
            for i in range(len(s)):
                if s[i] not in count_s:
                    count_s[s[i]]=1
                else:
                    count_s[s[i]]=1+count_s[s[i]]
                if t[i] not in count_t:
                    count_t[t[i]]=1
                else:
                    count_t[t[i]]=1+count_t[t[i]]
            if count_s==count_t:
                return True
            else:
                return False
