# least repeating character in a string

def least_char_occurrence(s):
    ch={}
    for i in s:
        if i in ch:
            ch[i] +=1
        else:
            ch[i]=1
    print(ch)
    result = min(ch, key = ch.get)
    print(result)

s = "aaabbbcccdddeeggggggi"
least_char_occurrence(s)

#count of any particular element
l = [1,2,4,6,3,2,1]
print(l.count(4))


def count_char_occurrence(s, search):
    ch={}
    for i in s:
        if i in ch:
            ch[i] +=1
        else:
            ch[i]=1
try:
    print(ch[search])
except:
    print("None")


s = "aaabbbcccdddeeggggggi"
count_char_occurrence(s,'j')