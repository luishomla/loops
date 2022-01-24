i=10
a=0
while i<=50:
    j=a
    while j<=i:
        if j%2!=0:
            print(j,end=" ")
        j+=1
    a+=10
    i+=10
    print()