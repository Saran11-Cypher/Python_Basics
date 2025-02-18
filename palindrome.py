def palindrome(n):
    while (True):
        s =0
        k = str(n)
        if(k == k[::-1]):
            break
        else:
            M = int(k[::-1])
            n +=M
            s +=1


    return n
print(palindrome(1473))