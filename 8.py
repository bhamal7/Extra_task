even_list = []
odd_list = []
for i in range(20):
    input1 = int(input("Please enter the number in the range of 1,50: "))
    if input1 % 2 == 0:
        even_list.append(input1)
    else:
        odd_list.append(input1)
    
    if len(even_list)==5 and len(odd_list)==5:
        break

print(even_list)
print(odd_list)
def sum_even(even_list):
    sum = 0
    for i in even_list:
        sum = sum + i
    return sum

def sum_odd(odd_list):
    sum = 0
    for i in odd_list:
        sum = sum + i
    return sum

print("Maximum of the list is ",max(sum_even(even_list),sum_odd(odd_list)))
