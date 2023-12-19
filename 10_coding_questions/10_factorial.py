def factorial(n):
    facto = 1
    for i in range(1, n+1):
        facto = facto*i
    return facto
# print(factorial(5))

def sum_of_facto(n):
    temp = n
    sum = 0
    while(temp > 0):
        digit = temp%10
        temp = temp//10
        facto = factorial(digit)
        sum = sum + facto
    if sum == n:
        print("yes")
    else:
        print("No")

sum_of_facto(1445)
