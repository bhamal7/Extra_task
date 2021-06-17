def Evenlength(s):
    for i in s.split(' '):
        if len(i) % 2 == 0:
            print(i)

x = Evenlength("hello my name is bishl")
print(x)