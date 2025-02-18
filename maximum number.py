def find_max(num1,num2):
    l = []
    max_number = -1
    if ( num1 < num2):
        for i in range( num1, num2 + 1):
            if (len(str(i))==2 and i % 15 == 0):
                l.append(i)
            if (len(l)!=0):
                max_number = max(l)
    return max_number
print(find_max(10,15))