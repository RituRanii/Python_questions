# def fibonnaci(n):
#  a=0
#  b=1
#  print(a)
#  while(b<n):
#    print(b)
#    a,b = b, a+b
# fibonnaci(10)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
n = 10
if n<=0:
    print(" invalid enter another one")
else:
    for i in range(n):
        print(fibonacci(i),end=" ")
