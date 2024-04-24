txt1="CALCULATOR"
txt2=txt1.center(180)
print(txt2)
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
Operation=int(input("Select any number from 1 to 4: "))
if Operation==1:
    print("Addition of",num1,"and",num2,"is: ",num1+num2)
elif Operation==2:
    print("Subtraction of",num1,"and",num2,"is: ",num1-num2)
elif Operation==3:
    print("Multiplication of",num1,"and",num2,"is: ",num1*num2)
elif Operation==4:
    print("Division of",num1,"and",num2,"is: ",num1/num2)
txt3="THANK YOU!!!"
txt4=txt3.center(180)
print(txt4)
    
