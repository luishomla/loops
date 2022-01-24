user=int(input("Enter a num:"))
store=user
i=1
sum=0
while i<user:
    if user%i==0:
        sum=sum+i
    i=i+1
if sum==store:
    print("Perfect number")
else:
    print("Not perfect number")
        









