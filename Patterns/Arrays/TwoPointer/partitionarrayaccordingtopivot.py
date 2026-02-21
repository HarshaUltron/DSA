from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        boolval=[False]*n
        nums2=[0]*n
        i=0
        j=n-1
        while i<j:
            if(nums[i]<pivot):
                nums2[i]=nums[i]
                boolval[i]=True
            elif(nums[i]>=pivot):
                nums2[j]=nums[i]
                boolval[j]=True
                j-=1

            i+=1    
        
        # for i in range(n):
        #     if boolval[i] is False:
        #         nums2[i]=pivot

        return nums2

df=Solution()
print(df.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))            


        