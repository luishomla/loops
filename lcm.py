num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
numbers_min=min(num1,num2)
while(1):
    if(numbers_min %num1==0 and numbers_min%num2==0):
        print("lcm of two numbers:",numbers_min)
        break
    numbers_min+=1 