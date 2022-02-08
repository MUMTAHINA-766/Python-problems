#sum in normal way

def sum_f(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i #every time goes to function and increases the value of i and sum with prevoius value
    return sum

num = input()
print(sum_f(int(num)))

#sum in recursive way

def sum_f2(n):
    if n == 0:
        return 0
    return n+sum_f2(n-1) # every time calls the function and add the (n-1) number with n

num = input()
print(sum_f2(int(num)))