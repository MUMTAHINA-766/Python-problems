# integer exponentiation
# 2^3 = 8, n^m = ?

def exponent(x, y):
    if y == 0:
        return 1
    else:
        return x*exponent(x, y-1)
print(exponent(2, 3))

#another way: for even and odd

def exponent(x, y):
    if y == 0:
        return 1
    if y%2 == 0:
        return exponent(x, y//2)*exponent(x, y//2)
    else:
        return x*exponent(x, y//2)*exponent(x, y//2)
print(exponent(4, 3))     
