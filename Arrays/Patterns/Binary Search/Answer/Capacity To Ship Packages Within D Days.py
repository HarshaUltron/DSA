class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left=max(weights)
        right=0
        for i in weights:
            right+=i
        
        while left<=right:
            mid=left+(right-left)//2
            r_sum=0
            dayss=1
            for i in weights:
                r_sum+=i
                if(r_sum>mid):
                    dayss+=1
                    r_sum=i
            if dayss<=days:
                
                right=mid-1
            else:
                left=mid+1
        return left                

        