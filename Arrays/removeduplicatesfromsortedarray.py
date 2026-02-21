arr=[1,1,2,2,2,3,3]
#Brute force
#convert it into set
arr=list(set(arr))
print(arr)

# T.C = O(n)

# S.C = O(n)

# also doesn't preserve order

ar1 = []
for j in arr:                # O(n)
    if j not in ar1:         # O(n) worst case each time
        ar1.append(j)        # O(1)
print(ar1)            
# Time Complexity: O(n²) (since in on list is linear)

# Space Complexity: O(n)

# Still preserves order ✅

# 🔹 Best Order-Preserving Solution

# Use a set to check membership in O(1):

ar1 = []
seen = set()
for j in arr:                # O(n)
    if j not in seen:        # O(1) avg
        ar1.append(j)        # O(1)
        seen.add(j)          # O(1)


# Time Complexity: O(n)

# Space Complexity: O(n)

# Preserves order ✅
