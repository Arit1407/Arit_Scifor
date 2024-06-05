"""
Question :-
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        s=""
        if len(digits)==1:
            n=digits[0]+1
            if n<10:
                digits[0]=n
                return digits
            else:
                digits.clear()
                s=str(n)
                for i in range(len(s)):
                    digits.append(int(s[i]))
                return digits
        else:
            for i in range(len(digits)):
                s+=str(digits[i])
            n=int(s)+1
            digits.clear()
            s=str(n)
            for i in range(len(s)):
                digits.append(int(s[i]))
            return digits
