from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            r_sum = 0

            for i in nums:
                r_sum += (i + mid - 1) // mid

            if r_sum <= threshold:
                # mid works, try smaller divisor
                right = mid - 1
            else:
                # mid doesn't work, need larger divisor
                left = mid + 1

        return left      

nums = [1,2,5,9]
threshold = 6
df=Solution()
print(df.smallestDivisor(nums,threshold))


  
        