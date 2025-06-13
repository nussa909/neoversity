

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        nonlocal cache
        
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)

        return cache[n]
    
    return fibonacci


fib = caching_fibonacci()

print(fib(10))  # Output: 55
print(fib(15))  # Output: 610
print(fib(0))  # Output: 0
print(fib(1))  # Output: 1
print(fib(-1))  # Output: 0