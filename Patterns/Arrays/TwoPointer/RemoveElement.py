from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        slow=0
        for high in range(0,n):
            if(nums[high]!=val):
                nums[slow],nums[high]=nums[high],nums[slow]
                slow+=1

        return nums[0:slow]        

nums=[3,2,2] 
val=3      
df=Solution()    
print(df.removeElement(nums,val))    