#second highest number in a list
# using for loop
def second_highest(n):
    if n[0]>n[1]:
        first = n[0]
        second = n[1]
    else:
        first = n[1]
        second = n[0]
    for i in range(2,len(n)):
        if n[i]>first:
            second = first
            first = n[i]
        elif n[i]>second and first!=l[i]:
            second = n[i]
    return second
l=[10,6,1,100,9]
print(second_highest(l))
