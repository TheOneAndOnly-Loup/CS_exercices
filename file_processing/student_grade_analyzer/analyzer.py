def avg(list):
    average=0
    for i in range(len(list)):
        average += list[i]
    average = average / len(list)
    return average

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

with open("random_grades.txt", "r") as file:
    grades = file.readlines()
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    # print(f"Average grade: {avg(grades)}/100")

    # print(f"Minimum value: {min(grades)}, Maximum value: {max(grades)}")

    count = sum(n >= 60 for n in grades)
    # print(f"Number of students passing: {count}")

    sorted_grades = quicksort(grades)
    # print(f"Sorted grade list: {sorted_grades}")

    # print(f"Index of grade 88: {binary_search(sorted_grades, 0, len(sorted_grades)-1, 88)}")

    with open("summary.txt", "w") as file:
        file.write(f"Average grade: {avg(grades)}/100, \nMinimum value: {min(grades)}, \nMaximum value: {max(grades)}, \nNumber of students passing: {count}, \nIndex of grade 88: {binary_search(sorted_grades, 0, len(sorted_grades)-1, 88)}")





