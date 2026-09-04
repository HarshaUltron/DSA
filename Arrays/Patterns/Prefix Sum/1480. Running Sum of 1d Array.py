# 1480. Running Sum of 1d Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum=[0]*(len(nums)+1)
        for i in range(0,len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]


        return prefix_sum[1:]   
        