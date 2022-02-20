# 0 1 1 2 3 5 8....

def fibo_recursive(n):
    if n<= 1:
        return n
    return fibo_recursive(n-1)+ fibo_recursive(n-2)

print(fibo_recursive(6))