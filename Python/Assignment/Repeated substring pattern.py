"""
Question :-
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 """
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        half = len(s) // 2
        
        for i in range(1, half+1):
            if len(s) % i != 0:
                continue
            
            substr = s[:i]
            
            if substr * (len(s)//i) == s:
                return True
        
        return False
