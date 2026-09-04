from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}
        for i in nums2:
            while stack and stack[-1]<i:
                element=stack.pop()
                next_greater[element]=i
            stack.append(i)
        for x in stack:
            next_greater[x]=-1
        return list(next_greater)
df=Solution()
a1 = [4, 1, 2]
a2 = [1, 3, 4, 2]
print(df.nextGreaterElement(a1,a2))                  

