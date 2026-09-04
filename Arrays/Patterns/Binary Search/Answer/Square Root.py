class Solution:
    def floorSqrt(self, n): 
        # code here
        left=1
        right=n
        k=0
        while left<=right:
            mid=left+(right-left)//2
            if((mid*mid)<=n):
                k=max(k,mid)
                left=mid+1
            else:
                right=mid-1
        return k        