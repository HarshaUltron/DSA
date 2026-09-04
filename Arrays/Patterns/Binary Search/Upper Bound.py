class Solution:
    def upperBound(self, nums, x):
        n=len(nums)
        left=0
        right=n-1
        k=n
        while(left<=right):
            mid=left+(right-left)//2
            if(nums[mid]>x):
                k=mid
                right=mid-1
            else:
                left=mid+1
        return k            

# Given a sorted array of nums and an integer x, write a program to find the upper bound of x.



# The upper bound of x is defined as the smallest index i such that nums[i] > x.



# If no such index is found, return the size of the array.


# Example 1

# Input : n= 4, nums = [1,2,2,3], x = 2

# Output:3

# Explanation:

# Index 3 is the smallest index such that arr[3] > x.

# Example 2

# Input : n = 5, nums = [3,5,8,15,19], x = 9

# Output: 3

# Explanation:

# Index 3 is the smallest index such that arr[3] > x.        