#Brute force
ar=[1,2,4,5]
ar=sorted(ar) # o(n log n)
print(ar[len(ar)-1]) 
#Time complexity -- > o(n log n)
#Space complexity --> o(n)


#optimal solution
arr=[1,4,7,2,25,123]
largest=arr[0]
for i in range(1,len(arr)):
    if(arr[i]>largest):
        largest=arr[i]

print(largest)   

#Time Complexity : o(n-1)

#space complexity : o(1)