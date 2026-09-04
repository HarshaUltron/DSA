from typing import List
print("hi")

class Solution:
    def twosum(self,target:int, nums:List[int])->List[int]:
        n=len(nums)
        dictt={}
        for i in range(0,n):
            complement=target-nums[i]
            if complement in dictt:
                return [dictt[complement],i]
            dictt[nums[i]]=i


df=Solution()
nums = [2,7,11,15]
target = 9
print(df.twosum(target,nums))
