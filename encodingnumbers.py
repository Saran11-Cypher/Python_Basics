def findingnumbers(numlist,n):
    count = 0
    for i in numlist:
        if(n-i!=i and n-1 in numlist ):
            count += 1
    if (count!=0):
        return count // 2
    else:
        return 0
numlist= [1,3,4,6,7,8,9]
n = 9
print(findingnumbers(numlist,n))