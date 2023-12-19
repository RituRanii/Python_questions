# by using split method
# def palindrome(s):
#     temp=s[::-1]
#     if s.split()==temp.split():
#         print("Yes!! It's Palindrome")
#     else:
#         print("No!! Not a Palindrome")

# s = "ritu"
# palindrome(s)

def is_palindrome(n):
    temp = n
    rev_n = 0
    while(temp>0):
        digit = temp%10
        print(digit)
        rev_n = rev_n*10 +digit
        temp = temp//10
    if n == rev_n:
        return True
    else:
        return False
n = 414
print(is_palindrome(n))
