# FIZZBUZZ PROBLEM
# IF NUM / BY 3 - PRINT FIZZ
# IF NUM / BY 5 - PRINT BUZZ
# IF NUM / BY 15 - PRINT FIZZBUSS
# ELSE PRINT NUM

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
        elif i%3==0:
            print("FIZZ")
        elif i%5==0:
            print("BUZZ")
        else:
            print(i)

fizzbuzz(10)