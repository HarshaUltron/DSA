# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1    

# Why do we stop when mid > high?

# “Because we maintain the invariant that elements beyond high are already 2s and elements before low are 0s. The region between mid and high is the only unprocessed part. Once mid crosses high, no unprocessed elements remain, so the array is fully sorted.”

# Clean. Precise. Confident.

# 🔎 Follow-Up Questions They May Ask
# 1️⃣ Why don’t we increment mid when swapping with high?

# Correct answer:

# Because the element swapped from high is unprocessed.
# It could be 0, 1, or 2.
# So we must re-evaluate it.

# If you increment mid there → you skip checking.

