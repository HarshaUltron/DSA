# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

arr= [1, 2, 0, 4, 3, 0, 5, 0]
# for i in range(1,len(arr)):
#     if(arr[i-1]==0):
#         arr[i],arr[i-1]=arr[i-1],arr[i]
print(arr.count(0))
for i in range(len(arr)):
    if(arr[i]==0):
        for j in range(i+1,len(arr)):
            if(arr[j]!=0):
                arr[i],arr[j]=arr[j],arr[i]
                break
print(arr)    
# T.C : O(n^2)
#S.C : O(1)

#optimal
#arr= [1, 2, 0, 4, 3, 0, 5, 0]
#pos=0, 
#
#

class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        pos = 0  # position to place the next non-zero
        
        # Step 1: Move non-zeros forward
        for i in range(n):  # O(n)
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Step 2: Fill remaining places with zeros
        while pos < n:      # O(n)
            arr[pos] = 0
            pos += 1

#T.C : O(n)
#S.C : O(1)