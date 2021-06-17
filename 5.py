string1 = "bishal"
print(string1[::-1])

#next way

def Reverse(string2):
    str = " "
    for i in string2:
        str = i+str
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print(i,end=' ')
    return str
print(Reverse("bishal"))