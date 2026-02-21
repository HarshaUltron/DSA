arr=[1,2,2,3,3,4]
ar=[1,2,1,3,4]
def issortede(arr):
    for i in range(1,len(arr)):
        if(arr[i]>=arr[i-1]):
            pass
        else:
            return False
    return True    

#print(issortede(ar))

# T.C : O(n)

# S.C : O(1)

#using recursion
def issorted(i, arr):
    if len(arr) <= 1:   # empty or single element
        return True
    if i == len(arr):
        return True
    if arr[i] >= arr[i-1]:
        return issorted(i+1, arr)
    else:
        return False
#T.C: O(n)

#S.C: O(n) (because recursion uses call stack)
      