from typing import List
nums=[2,7,11,15]
target = 18
class Solution:
 def twosum(self,nums:List[int],target) -> List:
  l=0
  r=len(nums)-1
  while(l<r):
   csum=nums[l]+nums[r]
   if csum==target:
    return [l+1,r+1]
   if csum<target:
    l=l+1  
   else:
    r=r-1

df=Solution()
k=df.twosum(nums,target)
print(k)