def majority_boyer_moore(arr):
    candidate, count = None, 0

    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Optional verification
    if arr.count(candidate) > len(arr)//2:
        return candidate
    return None

arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority_boyer_moore(arr))