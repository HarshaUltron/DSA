# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        low=0
        high=n-1
        mid=0
        while mid<=high:
            if nums[mid]<pivot:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==pivot:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

        return nums

df=Solution()
print(df.pivotArray([9,12,5,10,14,3,10], pivot = 10))