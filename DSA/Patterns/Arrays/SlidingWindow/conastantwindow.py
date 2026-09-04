arr=[-1,2,3,-15,4,5,-1]
k=4
#max sum you can obtain with 4 consecutive elements

#Brute Force
n=len(arr)
csum=0
msum=float('-inf')
p=n-k
for i in range(0,p):
   # print("i", i )
    csum=0
    for j in range(i,(i+k)):
        csum=csum+arr[j]
    #print(csum)    
    msum=max(csum,msum)
print(msum) 

#T.C : O(K)*O(K)
#S.C : O(1)

# Optimal Solution [TWO Pointer]
n = len(arr)
window_sum = sum(arr[:k])  # first window
max_sum = window_sum

l = 0
r = k

while r < n:
    window_sum = window_sum - arr[l] + arr[r]
    max_sum = max(max_sum, window_sum)
    l += 1
    r += 1

print(max_sum)

#T.C : O(K) + O(n-k) : o(n)
#S.C : O(1)




