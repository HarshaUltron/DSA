# Whenever you see:

# “subarray”
# “sum = k”

# 👉 Immediately think:
# Prefix Sum + HashMap

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}  # important

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in hashmap:
                count += hashmap[prefix_sum - k]

            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count
    

df=Solution()
print(df.subarraySum([1,1,1],2))    