def linearSearch(target, arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linearSearch(4, [1, 2, 3, 5, 6]))