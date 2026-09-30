def icecreamParlor(m, arr):
    for i in range(len(arr)):
        val1 = i
        for j in range(len(arr)):
            val2 = j
            if arr[val1] + arr[val2] == m:
                if val1 == val2:
                    continue
                return [i+1, j+1]

print(icecreamParlor(4, [1, 4, 5, 3, 2]))