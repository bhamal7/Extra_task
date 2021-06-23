
def SumPairs(x,n,sum):
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if x[i] + x[j] == sum:
                print(x[i],x[j],"\n")
                count+=1
    return count


x = [1,2,3,4,5,6,7,8,9,-1]
n = len(x)
sum = 8
obj = SumPairs(x,n,sum)
print(obj)