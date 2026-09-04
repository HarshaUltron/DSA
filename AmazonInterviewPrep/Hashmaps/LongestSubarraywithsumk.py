from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hashmap = {0: -1}  # important
        max_len = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if (prefix_sum - k) in hashmap:
                length = i - hashmap[prefix_sum - k]
                max_len = max(max_len, length)

            # store only FIRST occurrence
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i

        return max_len

df=Solution() 
arr= [10, 5, 2, 7, 1, -10]
k = 15    
print(df.longestSubarray(arr,k))