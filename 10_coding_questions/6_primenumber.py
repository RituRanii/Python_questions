# prime number using flag
# def prime_number(n):
#     flag = False
#     if n>1:
#         for i in range(2,n):
#             if (n % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         return "No! Its not a prime number"
#     else:
#         return "Yes! Its a prime number"
# print(prime_number(4))

#display prime numbers within a range.
def prime_number1(start,end):
    for n in range(start,end):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
                else:
                    print(n)

prime_number1(1,100)
