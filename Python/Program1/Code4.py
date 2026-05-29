# Coparision & Logical Operators

#Q1:Compare two numbers entered by the user and print if the first is greater than the second.
a=int(input("enetr num1:"))
b=int(input("enter num2:"))

c=a>b
print(c)

if (a>b):
    print(True)
else:
    print(False)


#Q2:Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result.
a=int(input("enter the num:"))

if (a%2==0):
    print(True)
    print(type(True))
else:
    print(False)
    print(type(False))


#Q3:Write a program that checks if a number is between 10 and 50 (inclusive) using and.
num1=40
result=num1>=10 and num1<=50

print(result)


#Q4:Check if a string entered by the user is equal to "Python".
name=str(input("enter your name:"))
result = (name == "Python")

print(result)


#Q5:Use the or operator to check if a user is either "Admin" or "Superuser".
name = str(input("Enter name: "))

if name == "Admin" or name == "Superuser":
    print("Access granted")
else:
    print("Access denied")


#Q6:. Demonstrate the not operator by reversing a Boolean variable. 
Love = True

print("Before:", Love)
print("After not:", not Love)


#Q7: Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result.
num = (0.1 + 0.2) == 0.3

print(num)


#Q8:Take a user's age and check if they are NOT under 18.
age = int(input("Enter your age: "))

if not (age < 18):
    print("You are 18 or older")
else:
    print("You are under 18")


#Q9: Check if a number is positive and odd using logical operators
num = int(input("Enter a number: "))

if num > 0 and num % 2 != 0:
    print("Number is positive and odd")
else:
    print("Condition not satisfied")


#Q10:Compare the lengths of two strings provided by the user.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > len(str2):
    print("First string is longer")
elif len(str1) < len(str2):
    print("Second string is longer")
else:
    print("Both strings have equal length")