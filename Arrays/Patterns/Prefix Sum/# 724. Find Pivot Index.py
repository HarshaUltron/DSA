# 724. Find Pivot Index
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum=[0]*(len(nums)+1)
        for i in range(0,len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        n=len(nums)
        for i in range(0,len(nums)):
            if(i==0):
                if(prefix_sum[n]-prefix_sum[i+1]==0):
                    return i

            elif(i==n-1):
                if(prefix_sum[n-1]==0):
                    return i
            else:
                right_sum=prefix_sum[n]-prefix_sum[i+1]
                left_sum=prefix_sum[i]
                if(right_sum==left_sum):
                    return i
        return -1                  

df=Solution()
print(df.pivotIndex([-1,-1,-1,1,1,1]))
        