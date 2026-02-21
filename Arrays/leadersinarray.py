class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)
        newl=[]
        count=0
        for i in range(n):
            count=0
            for j in range(i+1,n):
                if(arr[j]>arr[i]):
                    count=1
                    break
            if count==0:
                newl.append(arr[i])      

        return newl
    

arr = [16, 17, 4, 3, 5, 2]
df=Solution()
print(df.leaders(arr))


class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders_list = []
        
        max_from_right = arr[-1]  # rightmost element is always a leader
        leaders_list.append(max_from_right)

        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                leaders_list.append(arr[i])
                max_from_right = arr[i]

        # Since we traversed from right, reverse at the end
        leaders_list.reverse()
        return leaders_list

