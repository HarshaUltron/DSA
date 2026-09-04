def sort012(a):
    low, mid, high = 0, 0, len(a) - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:  # a[mid] == 2
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a
from typing import List
arr = [2, 0, 1, 2, 1, 0, 1, 2, 0]
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
            
            print(nums)
        #print(nums)
dd=Solution()
dd.sortColors(arr)
# Example

#print(sort012(arr))  # [0,0,0,1,1,1,2,2,2]
