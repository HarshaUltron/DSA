# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        slow=0
        for high in range(0,n):
            if(nums[high]!=val):
                nums[slow],nums[high]=nums[high],nums[slow]
                slow+=1
            
        print(nums)    
        return nums[0:slow]        

nums=[3,2,2,3] 
val=3      
df=Solution()    
print(df.removeElement(nums,val))    