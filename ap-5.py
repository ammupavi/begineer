num1=float(input("enter first num:"))
num2=float(input("enter second num:"))
num3=float(input("enter third num:"))
if(num1>num2) and (num1>num3):
    largest = num1
elif(num2>num1) and (num2>num3):
    largest = num2
else:
    largest = num3
print("The largest num is",largest)    
 
