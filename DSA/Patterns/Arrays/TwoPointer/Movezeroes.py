from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        k = 0  # pointer for the position to place the next non-zero

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1  # move to next zero position

        print(nums)

nums = [0, 1, 0, 3, 12]
df = Solution()
df.moveZeroes(nums)
