def string_format(s):
    l = []
    temp = s.split('_')
    for i in temp:
        l.append(i[0].lower()+i[1:].upper())
    s= '.'.join(l)
    print(s)
    
sen = "This_Is_A_Good_Morning_Text"
string_format(sen)
    