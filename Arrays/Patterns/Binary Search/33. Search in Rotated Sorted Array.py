from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid] == target:
              return mid

            # Is left half sorted?
            if nums[left] <= nums[mid]:

                # Does target belong to left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise right half is sorted
            else:

                # Does target belong to right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1            