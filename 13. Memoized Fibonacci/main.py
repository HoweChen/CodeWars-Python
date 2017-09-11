cache_fibonacci = {0: 0, 1: 1}


def fibonacci(n):
    if n in [0, 1]:
        return cache_fibonacci.get(n)
    else:
        if n in cache_fibonacci.keys():
            return cache_fibonacci.get(n)
        else:
            result = 0
            for i in range(2, n + 1):
                result = fibonacci(i - 1) + fibonacci(i - 2)
            cache_fibonacci[n] = result
    return cache_fibonacci.get(n)

print(fibonacci(70))
