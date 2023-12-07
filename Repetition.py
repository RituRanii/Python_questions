str = input("Enter your words:")
num = int(input("Enter the Count(N) for searching"))
str = str.split()
counts = dict()
for word in str:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
word_list=[]
for key in counts:
    if counts[key]>=num:
        word_list.append(key)
if len(word_list):
    print(word_list)
else:
    print("Na")
