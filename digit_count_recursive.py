#digit counting in recursive way

def digit_counter(n):
    if n == 0:
        return 0
    return 1+digit_counter(n//10)

print(digit_counter(1234574849092))