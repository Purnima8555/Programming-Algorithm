#1. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
# Cost price(in Rs)                  Tax
# >100000		                     15%
# >50000 and <=100000                10%
# <=50000                             5%
# cost=int(input("Enter the cost of bike: "))
# if cost>100000:
#     print(f"Your road tax is; {cost*0.15}")
# elif cost>50000 and cost<=100000:
#     print(f"Your road tax is; {cost*0.10}")
# elif cost<=50000:
#     print(f"Your road tax is; {cost*0.05}")
# else:
#     print("Error")


#2. Accept the age of 4 people and display the youngest one.
# user1=int(input("Enter your age: "))
# user2=int(input("Enter your age: "))
# user3=int(input("Enter your age: "))
# user4=int(input("Enter your age: "))
# if user1<user2 and user1<user3 and user1<user4:
#     print("User1 is the youngest")
# elif user2<user1 and user2<user3 and user2<user4:
#     print("User2 is the youngest")
# elif user3<user1 and user3<user2 and user3<user4:
#     print("User3 is the youngest")
# elif user4<user1 and user4<user2 and user4<user3:
#     print("User4 is the youngest")
# else:
#     print("Error")


#3. Accept the age of 4 people and display the oldest one.
# user1=int(input("Enter your age: "))
# user2=int(input("Enter your age: "))
# user3=int(input("Enter your age: "))
# user4=int(input("Enter your age: "))
# if user1>user2 and user1>user3 and user1>user4:
#     print("User1 is the oldest")
# elif user2>user1 and user2>user3 and user2>user4:
#     print("User2 is the oldest")
# elif user3>user1 and user3>user2 and user3>user4:
#     print("User3 is the oldest")
# elif user4>user1 and user4>user2 and user4>user3:
#     print("User4 is the oldest")
# else:
#     print("Error")


#4: Accept the percentage from the user and display the grade according to the following criteria:
# Below 25 --D
# 25 to 45  -- C
# 45 to 50 -- B
# 50 to 60 --B+
# 60 to 80 -- A
# Above 80 -- A+
# per=int(input("Enter your percentage: "))
# print(f"Percentage; {per}")
# if per<25:
#     print("D")
# elif per>=25 and per<45:
#     print("C")
# elif per>=45 and per<50:
#     print("B")
# elif per>=50 and per<60:
#     print("B+")
# elif per>=60 and per <80:
#     print("A")
# elif per<80:
#     print("A+")
# else:
#     print("Error")


#5. A company decided to give bonus to employee according to following criteria:
# Time period of service           Bonus
# More than 10 years	            10%
# >=6 and <=10                       8%
# Less than 6 years                  5%
# time=int(input("Enter the time duration: "))
# if time>10:
#     print("Your bonus is 10%")
# elif time>=6 and time<=10:
#     print("Your bonus is 8%")
# elif time<6:
#     print("Your bonus is 5%")
# else:
#     print("Invalid")


#6. Accept three numbers from the user and display the second largest number.
# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# num3=int(input("Enter 3rd number: "))
# if num1>num2>num3 or num3>num2>num1:
#     print(f"{num2} is the second largest.")
# elif num2>num1>num3 or num3>num1>num2:
#     print(f"{num1} is the second largest.")
# elif num1>num3>num2 or num2>num3>num1:
#     print(f"{num3} is the second largest.")
# else:
#     print("Error")


#7. Accept the number of days from the user and calculate the charge for library according to following:
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


#8. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for their salary and year of service and print the net bonus amount.
# salary=int(input("Enter the salary: "))
# time=int(input("Enter the years of service: "))
# if time>5:
#     print(f"Net bonus; {salary*0.05}")
# else:
#     print("You are not eligible for bonus")


#9. Write a program to check two strings are anagram or not.
# x=input("Enter first string: ")
# y=input("Enter second string: ")
# if sorted(x)==sorted(y):
#     print("They are anagrams.")
# else:
#     print("They are not anagrams.")


#10. 10. A school has following rules for grading system:
# Below 25 -F
# 25 to 45 - E
# 45 to 50 - D
# 50 to 60 - C
# 60 to 80 - B
# Above 80 - A
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

