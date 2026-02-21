from typing import List

class Solution:
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n-1)   # Step 1
        self.reverse(nums, 0, k-1)   # Step 2
        self.reverse(nums, k, n-1)   # Step 3
