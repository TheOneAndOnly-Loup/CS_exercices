def averageOfAnArray(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]

    average = sum/len(array)

    return average

def arrayCount(array, val):
    count = 0
    for i in range(len(array)):
        if array[i] == val:
            count += 1
    return count

def findMin(array):
    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min

def findMax(array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    return max

arr = [5,6,3,2,7,9,1,2,9,1,3,6,10,8]

print(f"The average of the array is {averageOfAnArray(arr)}")
v=2
print(f"The number of times {v} is in the provided array is {arrayCount(arr, v)}")
print(f"The minimum value in the provided array is {findMin(arr)} and the maximum value is {findMax(arr)}")
