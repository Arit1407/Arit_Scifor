"""
Question :-
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        if len(nums)==1 and nums[0]==0:
            return nums
        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    zero=nums[i]
                    nums.pop(nums.index(zero))
                    nums.append(zero)
            return nums
