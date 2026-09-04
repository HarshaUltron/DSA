from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        left = 0
        sliding_sum = 0

        for i in range(n):
            sliding_sum += nums[i]   # ✅ expand first

            while sliding_sum >= target:
                min_len = min(min_len, i - left + 1)  # ✅ correct length
                sliding_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
df=Solution()
print(df.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

#