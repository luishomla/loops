n=int(input("enter the number:"))
i=1
j=0
while i<=n:
    if n%i==0 and n%n==0:
        j=j+14
    i=i+1
if j==2:
    print("prime no.")
else:
    print("not prime no.")

