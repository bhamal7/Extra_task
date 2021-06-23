tuple1 = (1,2,3,4,5,6,7,8,9,10)
list1 = list(tuple1)
listtemp = []
for i in list1:
    if i % 2 == 0:
        listtemp.append(i)
final_temp = tuple(listtemp)
print(final_temp)
