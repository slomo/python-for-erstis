def fibonacci(n):
    if (n < 2):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(3))
print(fibonacci(10))
print(fibonacci(-1))
