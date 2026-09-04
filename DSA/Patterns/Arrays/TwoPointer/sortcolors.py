from typing import List
class Solution:
    def sortcolors(self,nums:List[int])-> List[int] :
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while mid<=high:
                if nums[mid]==0:
                    nums[low],nums[mid]=nums[mid],nums[low]
                    low=low+1
                    mid=mid+1
                elif nums[mid]==1:
                    mid=mid+1
                else:
                    nums[mid],nums[high]=nums[high],nums[mid]
                    high=high-1 
        return nums

nums = [2,0,2,1,1,0]
df=Solution()
print(df.sortcolors(nums))