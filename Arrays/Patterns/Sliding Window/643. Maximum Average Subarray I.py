# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        sliding_sum=sum(nums[:k])
        maxavg=sliding_sum/k
        for i in range(k,n):
            sliding_sum+=nums[i]
            sliding_sum-=nums[i-k]
            maxavg=max(sliding_sum/k,maxavg)
        return maxavg

df=Solution()
print(df.findMaxAverage([1,12,-5,-6,50,3], k = 4))        



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        c_sum = 0
        max_avg = float('-inf')

        for right in range(len(nums)):
            c_sum += nums[right]

            

            if right - left + 1 == k:
                max_avg = max(max_avg, c_sum / k)

            if right - left + 1 > k:
                c_sum -= nums[left]
                left += 1    

        return max_avg