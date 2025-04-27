# Write a program to input user first name & print its length.
name = input("Enter the first name of the user: ")
print("length of your name is: ",len(name))



# Write a program to find the occurance of '$' in a string.
str = "This is my $ pen"
print(str.count("$"))


# Write a program to input user marks of student based on grade
marks = int(input("Enter the marks of the student: "))

if(marks >= 90):
    grade = "A"
    
elif(marks >= 80 and marks < 90):
    grade = "B"
    
elif(marks >= 70 and marks < 80):
    grade = "C"
    
elif(marks <= 70):
    grade = "D"
    
else:
    print("Fail")
    
print("grade of the student: ",grade)


# Write a program to input user marks of student based on grade ny using another method
marks = int(input("Enter the marks of the student: "))

if(marks >= 90):
    print("A")
    
elif(marks >= 80 and marks < 90):
    print("B")
    
elif(marks >= 70 and marks < 80):
    print("C")
    
elif(marks <= 70):
    print("D")
    
else:
    print("Fail")
    
    
    
# Write a program to check if the number enter by the user is odd or even.
num = int(input("Enter the number: "))

if(num%2 == 0):
    print("The given number is even: ",num)
    
else:
    print("The given number is odd: ",num)
    
    
# Write a program to gratest of three numbers entered by the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if(num1 >= num2 and num1 >= num3):
    print("The first largest number is: ",num1)
    
elif(num2 >= num3 and num2 >= num1):
    print("The Second largest number is: ",num2)
    
elif(num3 >= num1 and num3 >= num1):
    print("The Third largest number is: ",num3)
    

# Write a program to check if a number is multiple of 7 or not.
num = int(input("Enter the number: "))

if(num%7 == 0):
    print("multiple of 7 is: ",num)
else:
    print("not a multiple")