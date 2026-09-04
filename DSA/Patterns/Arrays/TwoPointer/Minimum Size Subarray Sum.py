# from typing import List
# from typing import List

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         minlen = float('inf')
#         n = len(nums)

#         for i in range(n):
#             curr_sum = 0
#             for j in range(i, n):
#                 curr_sum += nums[j]
#                 if curr_sum >= target:
#                     minlen = min(minlen, j - i + 1)
#                     break

#         return 0 if minlen == float('inf') else minlen

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        minlen = float('inf')

        for right in range(len(nums)):
            print(right)
            curr_sum += nums[right]

            while curr_sum >= target:
                minlen = min(minlen, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if minlen == float('inf') else minlen

df=Solution()
print(df.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))    