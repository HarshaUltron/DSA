from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        val_list=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(nums[i]+nums[j]+nums[k])==0:
                        val_list.append([nums[i],nums[j],nums[k]])

        return val_list
    

nums = [0,0,0]   
df=Solution()
ans=df.threeSum(nums)
print(ans)