#highest common factor between two numbers(factor-if a is divided by b then b is a factor)

def HCF(a, b):
    if a>b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller+1):
        if a % i == 0 and b % i == 0:
            ans = i
            print(ans)
    return ans
    
HCF(int(input()), int(input()))

