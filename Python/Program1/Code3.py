#Q1:write a program to caculate the area of rectangle(lenght X width).
length=int(input("enter your length:"))
width=int(input("enter your width:"))
print("Area of rectangle is:",length*width)

#Q2:take two numbers and print the result of firest raised to the power of second(a^b).
a=int(input("enter your num:"))
b=int(input("enter your num2:"))
result=a**b
print(result)

#Q3:Demonstrate the dif bw /(div) and \(floor divison) with the numbers 10 and 3.
num1=10
num2=3
result1=num1/num2
result2=num1//num2
print(result1)
print(result2)

#Q4:Use modules operator % to find the reminder when 25 is divided by 4.
num1=25
num2=4
reminder=num1%num2
print(reminder)

#Q5:caculate the average of five numbers entered by the user.
a=int(input("enter your num:"))
b=int(input("enter your num:"))
c=int(input("enter your num3:"))
d=int(input("enter your num4:"))
e=int(input("enter your num5:"))
average=(a+b+c+d+e)/5
print(average)

#Q6:Create a program that converts minutes into hours and remaining minutes.
total_minutes=int(input("enter your minutes:"))
Hours=total_minutes//60
minutes=total_minutes%60
print(Hours,minutes)

#Q7:Calculate the area of a circle where Area = \pi r^2 (Use 3.14 for \pi).
r=int(input("enter your radius:"))
Area=3.14*r*r
print(Area)

#Q8:Find the cube of a number entered by the user.
a=float(input("enter the value:"))
print(a**3)

#Q9:Perform the calculation 10 + 5 * 2. Does Python follow PEMDAS? Prove it with code.
a=10+5*2
print(a)

#Q10:Write a program to calculate simple interest: (P /R / T) / 100.
p=int(input("enter p:"))
r=int(input("enter r:"))
t=int(input("enter t:"))
si=(p*r*t)/100
print(si)