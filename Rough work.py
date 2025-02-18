def largestnumber(numlist):
    s = 0
    while (len(numlist)!=0):
        s = s * 100 + max(numlist)
        numlist.remove (max(numlist))
    return s
numlist = [23,34,57]
largernumber = largestnumber(numlist)
print(largestnumber)
