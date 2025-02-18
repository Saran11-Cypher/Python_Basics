def findtheproduct(a,b,c):
    product = 0
    if(a == 7):
        product = a * b
    elif ( b == 7):
        product = c
    elif (c == 7):
        product = -1
    else:
        product = a * b * c
    return product
print(findtheproduct(2,4,5))
print(findtheproduct(1,7,6))
print(findtheproduct(5,6,7))
