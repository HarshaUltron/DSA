from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        sliding_sum=float(0)
        max_avg=float("-INF")
        for i in range(0,k):
            sliding_sum+=nums[i]
        max_avg=max((sliding_sum)/k,max_avg)
        for i in range(k,n):
            sliding_sum-=nums[i-k]
            sliding_sum+=nums[i]
            max_avg=max((sliding_sum)/k,max_avg)
        return max_avg    
    
df=Solution()
print(df.findMaxAverage([1,12,-5,-6,50,3], k = 4))    