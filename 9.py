from collections import Counter

alphanumeric_string = "12abcbacbaba344ab"
str_int=[]
str_alp = []
for i in alphanumeric_string:
    if i.isalpha():
        str_alp.append(i)
    else:
        str_int.append(i)

print(str_int)
print(str_alp)

print(Counter(str_alp))
