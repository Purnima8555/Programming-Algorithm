#1: Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# if a==b:
#     print(1)
# elif a>b:
#     print(2)
# else:
#     print(3)


#2: Print "Hello" if a is equal to b or if c is equal to d.
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# d=int(input("Enter a number: "))
# if a==b or c==d:
#     print("Hello")
# else:
#     print("Invalid")


#3: Print "Hello" if a is equal to b, and c is equal to d.
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# d=int(input("Enter a number: "))
# if a==b and c==d:
#     print("Hello")
# else:
#     print("Invalid")


#4: For given integer x, print 'True' if it is positive, print 'False' if it is negative and print 'zero' if it is 0.
# x=int(input("Enter a number: "))
# if x>0:
#     print("True")
# elif x==0:
#     print("It is 0")
# else:
#     print("False")


#5: Check whether the user input number is even or odd and display it to user.
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print(f"{num} is an even number.")
# else:
#    print(f"{num} is an odd number.")


#6: WAP which accepts marks of four subjects and display total marks, percentage and grade.
# [Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail]
# nepali=int(input("Enter your marks: "))
# english=int(input("Enter your marks: "))
# maths=int(input("Enter your marks: "))
# science=int(input("Enter your marks: "))
# total=nepali+english+maths+science
# print(f"total_marks; {total}")
# per=total/4
# print(f"percentage; {per}")

# if per>=70:
#     print("Distinction")
# elif per<70 and per>=60:
#     print("First division")
# elif per<60 and per>=40:
#     print("Pass")
# else:
#     print("Fail")


#7: What is the output of 'APPLE'>'apple'?
# 'APPLE'>'apple'


#8: Write a Python program to display your details like name, age, address in three different lines.
# print("My name is Purnima Rana, \nI am 18 years old, \nI live in Hadigaun.")


#9: Write a python program which accepts the radius of circle from user and compute the area.
# r=int(input("Enter a radius: "))
# print(f"Area of circle;{22/7*r**2}")


#10:  A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of 
# students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers:
#  the number of students in each of the three classes, a, b and c respectively.
# Hint:[In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, 
# so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.]


#11: Write a python program which calculates tax of an employee with given condition:
    # Salary            	       Tax Rate
    # Below 20000                  15%
    # 20000 to 50000               25%
    # 50000 to 100000              30%
    # Above 100000                 35%


#12: Given three integers, print the smallest one. (Three integers should be user input)
# x=int(input("Enter 1st number: "))
# y=int(input("Enter 2nd number: "))
# z=int(input("Enter 3rd number: "))
# if x<y and x<z:
#     print('Smallest integer is x')
# if y<x and y<z:
#     print('Smallest integer is y')
# if z<x and z<y:
#     print('Smallest integer is z')


#13: N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each 
# single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.


#14: Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
# list=[1,2,3,4,5]


#15: Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 
# 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display 
# an error message if the user enters a number that is outside the range of 1 to 12.
# num=int(input("Enter a number: "))
# if num==1:
#     print("January")
# elif num==2:
#     print("Feburary")
# elif num==3:
#     print("March")
# elif num==4:
#     print("April")
# elif num==5:
#     print("May")
# elif num==6:
#     print("June")
# elif num==7:
#     print("July")
# elif num==8:
#     print("August")
# elif num==9:
#     print("September")
# elif num==10:
#     print("October")
# elif num==11:
#     print("November")
# elif num==12:
#     print("December")
# else:
#     print("Error")


#16: Given x = 5, what will be the value of x after we run x+=3?
# x=5
# x+=3
# print(x)


