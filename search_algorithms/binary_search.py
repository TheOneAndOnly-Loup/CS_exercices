def binarySearch(target, arr):
    low=0
    upper=len(arr)-1

    while low<=upper:
        mid_index = low + (upper - low) // 2
        mid=arr[mid_index]
        if mid==target:
            return mid_index
        elif mid<target:
            low=mid_index+1
        else:
            upper=mid_index-1 
    return -1

print(binarySearch(9,[-1,0,3,5,9,12]))