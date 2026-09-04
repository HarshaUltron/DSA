# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
# from typing import List
# import math
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         cnt=0
#         for i in range(n):
#             if nums[i]<k:
#                 cnt+=1
#         for i in range(2,n+1):
#             windows_prod=math.prod(nums[:i])
#             if(windows_prod<k):
#                     cnt+=1
#             for j in range(i,n):
#                 windows_prod*=nums[j]
#                 windows_prod/=nums[j-i]
#                 if(windows_prod<k):
#                     cnt+=1
#         return cnt            

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):

            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            count += right - left + 1

        return count
df=Solution()
print(df.numSubarrayProductLessThanK([10,5,2,6],100))