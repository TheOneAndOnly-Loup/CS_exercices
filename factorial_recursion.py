def factorial(n):
    global times
    if n <= 1:
        return 1
    times += 1
    print(times)
    return n * factorial(n-1)

times = 0
print(factorial(998))