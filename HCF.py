# a=int(input("enter first number:"))
# b=int(input("enter second  number:"))
# while a%b!=0:
#     rem=a%b
#     a=b
#     b=rem
# print("HCF is",b)



num1=int(input("enter the num:"))
num2=int(input("enter the num:"))
rem=1
if num1>num2:
    while rem!=0:
        rem=num1%num2
        if rem==0:
            hcf=num2
        else:
            num1=num2
            num2=rem
else:
    while rem!=0:
        rem=num2%num1
        if rem==0:
            hcf=num1
        else:
            num2=num1
            num1=rem
        print("HCF of two num is:",hcf)