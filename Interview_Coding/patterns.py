def full_pyramid():
    for i in range(1,8):
        for j in range(8-i):
            print(" ", end=" ")
        k=1
        while True:
            print("*", end=" ")
            k+=1
            if (k > 2*i -1): 
                break
        print()
        
def inverted_pyramid():
    for l in range(8,0,-1):
        for p in range(8-l):
            print(" ", end=" ")
        N = 1
        while True:
            print("*", end=" ")
            N+=1
            if (N>2*l-1):
                break
        print()
    print("Diamond with odd Multiples.")

def Normal_diamond():
    for i in range(1,8):
        for j in range(8 - i):
            print("", end =" ")
        for k in range(1, i):
            print("*", end=" ")
        print()
    
    for o in range(8,0,-1):
        for p in range(8 -o):
            print("", end=" ")
        for u in range(1,o):
            print("*", end=" ")
        print()
    print("Diamond with normal 8 triplet.")


def while_pyramid():
    i=8
    while i>0:
        j = 0
            print(" ", end=" ")
            j+=1
        k=1
        while True:
            print("*",end=" ")
            k+=1
            if(k>2*i-1):
                break
        print()
        i-=1
while_pyramid()
        