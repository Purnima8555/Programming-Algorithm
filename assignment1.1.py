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
# print('APPLE'>'apple')
# output:False


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
# salary=int(input("Enter the salary: "))
# if salary<20000:
#     print(f"Net salary; Rs.{salary-(salary*0.15)}")
# elif salary>=20000 and salary<50000:
#     print(f"Net salary; Rs.{salary-(salary*0.25)}")
# elif salary>=50000 and salary<100000:
#     print(f"Net salary; Rs.{salary-(salary*0.30)}")
# elif salary>=100000:
#     print(f"Net salary; {salary-(salary*0.35)}")
# else:
#     print("Error")


#12: Given three integers, print the smallest one. (Three integers should be user input)
# x=int(input("Enter 1st number: "))
# y=int(input("Enter 2nd number: "))
# z=int(input("Enter 3rd number: "))
# if x<y and x<z:
#     print('Smallest integer is x')
# elif y<x and y<z:
#     print('Smallest integer is y')
# elif z<x and z<y:
#     print('Smallest integer is z')
# else:
#     print("Error")


#13: N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each 
# single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.
# s=int(input("Enter the number of students: "))
# a=int(input("Enter the number of apples: "))


#14: Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
# list=[1,2,3,4,5]
# if 5 in list:
#     print("It is in the list")
# else:
#     print("It is not in the list")


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
# output:8


#17: A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
# marks=int(input("Enter your total marks: "))
# per=marks/4
# print(f"percentage; {per}")
# if per<25:
#     print("F")
# elif per>=25 and per<45:
#     print("E")
# elif per>=45 and per<50:
#     print("D")
# elif per>=50 and per<60:
#     print("C")
# elif per>=60 and per<80:
#     print("B")
# elif per>80:
#     print("A")
# else:
#     print("Error")


#18: Take input of age of 3 people by user and determine oldest and youngest among them.
# user1=int(input("Enter your age(user1): "))
# user2=int(input("Enter your age(user2): "))
# user3=int(input("Enter your age(user3): "))
# if user1>user2 and user1>user3:
#     print("User1 is the oldest")
# else:
#     print("User1 is the youngest")
# if user2>user1 and user2>user3:
#     print("User2 is the oldest")
# else:
#     print("User2 is the youngest")
# if user3>user1 and user3>user2:
#     print("User3 is the oldest")
# else:
#     print("User3 is the youngest")



#19: Write a program to check whether a person is eligible for voting or not. (accept age from user)
# age=int(input("Enter your age: "))
# if age=<18:
#     print("You are not eligible to vote")
# else:
#     print("You are eligible to vote")


#20: Write a program to check whether a number is divisible by 7 or not.
# num=int(input("Enter a number: "))
# if (num % 7)== 0:
#     print("It is divisible by 7")
# else:
#     print("It is not divisible by 7")


#21: Accept any city from the user and display monument of that city.
#   City                                 Monument
#   Delhi                               Red Fort
#   Agra                                Taj Mahal
#   Jaipur                              Jal Mahal
# city=input("Enter name of city: ")
# if city=="Delhi":
#     print("Fort")
# elif city=="Agra":
#     print("Taj")
# elif city=="Jaipur":
#     print("Jal Mahal")
# else:
#     print("Error")


#22: Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
# num=int(input("Enter a number: "))
# if (num%2)==0 and (num%3)==0:
#     print("It is divisible by 2 and 3")
# else: 
#     print("It is not divisible by 2 and 3")


#23: Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16
# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# operator=input("Enter operator[+,-,*,%]: ")
# if operator=="+":
#     print(f"Addition; {num1+num2}")
# elif operator=="-":
#     print(f"Subtraction; {num1-num2}")
# elif operator=="*":
#     print(f"Multiplication; {num1*num2}")
# elif operator=="%":
#     print(f"Division; {num1/num2}")
# else:
#     print("Error")


#24: Write the syntax of simple if-statement.
# The syntax for if-statement is as follows: if (condition) instruction; The condition evaluates to either true or false.
# True is always a non-zero value, and false is a value that contains zero.If the Boolean expression evaluates to true, then the block of code inside
#  the 'if' statement will be executed.


#25: Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
# num=int(input("Enter a number: "))
# if (num%5)==0:
#     print("Hello")
# else:
#     print("Bye")


#26: Write a program to accept a number from 1 to 7 and display the name of the day like 1 for sunday, 2 for monday and so on.
# num=int(input("Enter a number: "))
# if num==1:
#     print("Sunday")
# elif num==2:
#     print("Monday")
# elif num==3:
#     print("Tuesday")
# elif num==4:
#     print("Wednesday")
# elif num==5:
#     print("Thursday")
# elif num==6:
#     print("Friday")
# elif num==7:
#     print("Saturday")
# else:
#     print("Error")


#27: Write the logical expression for the following:
# A is greater than B and C is greater than D
# (A>B && C>D)


#28: Write a program to check whether a number entered is three digit number or not.
# num=int(input("Enter a number: "))
# if num>=100 and num<1000:
#     print("It is a three-digit number")
# else:
#     print("It is not three-digit number")


#29: Write a program to check whether a person is senior citizen or not.
# age=int(input("Enter your age: "))
# if age>=60:
#     print("You are a senior citizen")
# else:
#     print("You are not a senior citizen")


#30: Write a program to find the lowest number out of two numbers expected from user.
# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# if num1<num2:
#     print("1st number is the lowest number")
# elif num1>num2:
#     print("2nd number is the lowest number" )
# else:
#     print("Error")


#31: Out of "elif" and "else if",  which is the correct statement in python?
# "Elif" is the correct statement in python.


#32: Accept the following from the user and calculate the percentage of class attended:
# a. Total number of working days
# b. Total number of days for absent
# After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.
# w_days=int(input("Enter the number of working days: "))
# a_days=int(input("Enter the number of absent days: "))
# total_days= (w_days+a_days)
# per= (w_days/total_days)*100
# print(f"Percentage of working days; {per}")
# if per>=75:
#     print("You are eligible to sit in exam")
# else:
#     print("You are not eligible to sit in exam")


#33:  Write a program to accept percentage and display the category according to the following criteria:
# Percentage                    Category
# <40		                      Failed
# >=40 and <55                    Fair
# >=55 and <65	                  Good
# >=65		                     Excellent	
# marks=int(input("Enter your total marks: "))
# per=marks/5
# print(f"percentage; {per}")
# if per<40:
#     print("Failed")
# elif per>=40 and per<55:
#     print("Fair")
# elif per>=55 and per<65:
#     print("Good")
# elif per>=65:
#     print("Excellent")
# else:
#     print("Error")


#34:  Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
# Age		     Sex     	   Wage/day
# >=18 and <30    M	             700
# 		          F	             750
# >=30 and <=40	  M	             800
# 		          F	             850
# age=int(input("Enter your age: "))
# sex=input("Enter your sex[M,F]: ")
# work_days=int(input("Enter your work days: "))
# if age>=18 and age<30 and sex=="M":
#     print(f"Your wage is", {700*work_days})
#     if sex=="F":
#         print(f"Your wage is", {750*work_days})
# elif age>=30 and age<=40 and sex=="M":
#     print(f"Your wage is", {800*work_days})
#     if sex=="F":
#         print(f"Your wage is", {850*work_days})
#     else:
#         print("You are not eligible for thr job")


#35: Accept three numbers from the user and display the second largest number.
# num1=int(input("Enter the 1st number: "))
# num2=int(input("Enter the 2nd number: "))
# num3=int(input("Enter the 3rd number: "))
# if num1>num2 and num1>num3:
#     if num2>num3:
#         print("The second largest number is", num2)
#     else:
#         print("The largest number is", num3)
# elif num2>num1 and num2>num3:
#     if num1>num3:
#         print("The second largest number is", num1)
#     else:
#         print("The largest number is", num3)
# else:
#     if num1>num2:
#         print("The second largest number is", num1)
#     else:
#         print("The second largest number is", num2)


#36: Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day
# days=int(input("Enter the number of days: "))
# if days<=5:
#     print(f"Amount; Rs.{2*days}")
# elif days>=6 and days<=10:
#     print(f"Amount; Rs.{3*days}")
# elif days>=11 and days<=15:
#     print(f"Amount; Rs.{4*days}")
# elif days<=15:
#     print(f"Amount; Rs.{5*days}")
# else:
#     print("Cannot be kept for too many days") 


#37: Evaluate the following statements:
# a=True
# b=True
# c=True
# d=True
# print(c)
# print(d)
# print(not a)
# print(not b)
# print(not c)
# print(not d)
# print(a and b)
# print(a or b)
# print(a and b or c)
# print(not a or b or c)
# print(not a or not b or not c)
# print(not(not a or not b or not c))

# output:
# True
# True
# False
# False
# False
# False
# True
# True
# True
# True
# False
# True


#10, 13, 18, 34