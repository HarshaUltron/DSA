# from typing import List

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         prefix_sum=0
#         freq={}
#         count=0
#         freq[0]=1
#         for num in nums:
#             prefix_sum+=num
#             count+=freq.get((prefix_sum-k),0)
#             freq[prefix_sum]=freq.get(prefix_sum,0)+1
#         return count    
        

# df=Solution()
# print(df.subarraySum([1,1,1], k = 2))

a=-2
k=5       
print((a%k))