def bubbleSort(array):
    for i in range(len(array)):
        flag = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:
            break
    return array

data = [-2, 45, 0, 11, -9]

print(bubbleSort([-9, -2, 0, 11, 45]))