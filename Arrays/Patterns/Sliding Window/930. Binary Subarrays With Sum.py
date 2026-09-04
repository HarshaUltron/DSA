# 930. Binary Subarrays With Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length

def atMost(nums, goal):
    if goal < 0:
        return 0

    left = 0
    curr_sum = 0
    res = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > goal:
            curr_sum -= nums[left]
            left += 1

        res += (right - left + 1)

    return res


class Solution:
    def numSubarraysWithSum(self, nums, goal):
        return atMost(nums, goal) - atMost(nums, goal - 1)
    


class Solution:
    def numSubarraysWithSum(self, nums, goal):
        c_sum=0
        left=0
        res=0
        for right in range(0,len(nums)):
            c_sum+=nums[right]
            while (c_sum>goal):
                c_sum-=nums[left]
                left+=1
        if(c_sum==goal):
            res+=1
        return res                