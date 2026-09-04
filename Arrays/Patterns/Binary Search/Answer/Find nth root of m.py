class Solution:
    def nthRoot(self, n, m):
        left=0
        right=m
        while(left<=right):
            mid=left+(right-left)//2
            if((mid**n)==m):
                return mid
            if((mid**n)>m):
                right=mid-1
            else:
                left=mid+1
        return -1               
      
