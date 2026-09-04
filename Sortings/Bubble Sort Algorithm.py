class Solution:
    def BubbleSort(self,n,arr):

        for i in range(0,n):
            for j in range(0,n-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]

        return arr           
n = 6
arr = [13,46,24,52,20,9]
df=Solution()
print(df.BubbleSort(n,arr))

"""
#Time Complexity : Best and worst case : O(n^2)
#Space Complexity : O(1)
"""
#Optimal

class Solution:
    def BubbleSort(self,n,arr):

        for i in range(0,n):
            swapped=False
            for j in range(0,n-i-1):
                if(arr[j]>arr[j+1]):
                    swapped=True
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            if not swapped:
                return arr
        return arr           
n = 6
arr = [13,46,24,52,20,9]
df=Solution()
print(df.BubbleSort(n,arr))

"""
#Time Complexity : Best Case : O(1) and worst case : O(n^2)
#Space Complexity : O(1)

"""



