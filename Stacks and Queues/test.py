class Solution:
    def nextSmallerEle(self, arr):
        stack=[]
        next_smaller={}
        for index,i in enumerate(arr):
            print(index,i)
            while stack and nums[stack[-1]]<i:
                ele=stack.pop()
                next_smaller[i]=index
            stack.append(i)    

df=Solution()
nums = [4, 8, 5, 2, 25]
print(df.nextSmallerEle(nums))