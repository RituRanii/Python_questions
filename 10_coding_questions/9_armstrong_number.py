def armstrong(n):
    sum = 0
    temp = n
    while temp >0:
        digit = temp %10
        sum = sum + (digit**3)
        temp = temp//10
    if n == sum:
        print("yes")
    else:
        print("No")
n = 153
armstrong(n)