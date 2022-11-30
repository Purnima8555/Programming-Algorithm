#FOR LOOP QUESTION ANSWERS:

#1. Print "softwarica" 10 times:
# a="softwarica"
# for i in range(1,11):
#     print(a)

#OR

# for i in range(1,11):
#     print("softwarica")


#2. Sum of list:
# sum=0
# a=int(input("Enter a number: "))
# b=str(a)
# for i in b:
#     sum= sum + int(i)
# print(sum)


#3. Print each character using indexing:
# a="Python"
# b=len(a)
# print(b)
# for i in range(b):
#     print(i,'=',a[i])


#4. Program to display each element of a list:
# list=[1,2,3,4,5]
# for item in list:
#     print(item)

#OR 

# list=[1,2,3,4,5]
# for i in list:
#     print(i)


#5. multiplication of each element:
# multiplication=1
# a=int(input("Enter number: "))
# b=str(a)
# for i in b:
#     multiplication=multiplication*int(i)
# print(multiplication)


#6. multiplication table of a given number:
# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num,'*',i,'=',num*i)


#7. reverse a list:
# list=[1,2,3,4,5,6]
# reversed_list=[]
# for value in list:
#     reversed_list=[value]+reversed_list
# print("Reversed list:",reversed_list )

#OR

# a=[ 1,2,3,4,5,6 ]
# b=str(a)
# reverse_string=" "
# for i in b:
#     reverse_string=i+reverse_string
# print(reverse_string)

# 7. reverse string:
# list="12345"
# reverse_string=""
# for i in list:
#    reverse_string=i+reverse_string
# print(reverse_string)


#8. Program to count the tottal number of digits in a number:
# digit=0
# a=int(input("Enter number: "))
# b=str(a)
# for i in b:
#     if i.isdigit():
#         digit=digit+1
#     else:
#         pass
# print(digit)

#OR

# digit=0
# a=input("Enter number: ")
# for i in a:
#     if i.isdigit():
#         digit=digit+1
#     else:
#         pass
# print(digit)


#9. Given number is prime or not:
# a=int(input("Enter a number; "))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")
# else:
#     print("It is not a prime number")


#10. Python program to count the number of even and odd numbers from a series of numbers: [to find even and odd within the range of numbers]
# a=int(input("Enter series of number: "))
# odd=0
# even=0
# for i in range(a):
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
      
# print(even)
# print(odd)
    

#11. Pyhton program that accepts a string and calculate the number of digites and letters:
# a=input("Enter: ")
# digit=0
# letter=0
# for i in a:
#     if i.isdigit():
#         digit=digit+1
#     elif i.isalpha():
#         letter=letter+1
#     else:
#         pass
# print(digit)
# print(letter)


#12. Pyhton program to check the validity of username and password input by users:
# username="Ram"
# password=1234
# for i in range(3):
#     username1=input("Enter valid username: ")
#     password1=int(input("Enter valid password: "))
#     if username==username1 and password==password1:
#         print("Logged in")
#         break
#     else:
#         print("Invalid credentials")
# else:
#     print("3 attempts finished")

#AND:

# username="Ram"
# password=1234
# for i in range(1):
#     username1=input("Enter valid username: ")
#     password1=int(input("Enter valid password: "))
#     if username==username1 and password==password1:
#         print("Logged in")
#         break
# else:
#     print("Invalid username or password")


#13. Program to print the given number is odd or even:
# for i in range(1):
#     a=int(input("Enter a number: "))
#     b=a%2
#     if b==0:
#        print({a},"is an even number")
#        break
# else:
#        print({a},"is an odd number")


#14. Factorial of a given number:
# a=int(input("Enter a number: "))
# factorial=1
# for i in range(1,a+1):
#     factorial=factorial*i       
# print(factorial)


#15. Program to check given number is palindrome or not:
# a=int(input("Enter a number: "))



#16. Pyhton program to check given number is armstrong or not:
#17. Pyhton program to check a number is perfect square or not:
# num=int(input("Enter the number: "))


#18. Pyhton program to check a number is perfect number or not: [perfect number:6,28,496,8128]
# num=int(input("Enter a number: "))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+1
# if(sum==num):
#      print("The number is perfect number")
# else:
#      print("The number is not perfect number")


#19. Print multiplication table of 1,2,3,4,5,6,7,8
# for i in range(1,9):
#     print(i)
#     for j in range(1,11):
#         print(i*j)

# for i in range(1,11):
#     print(i)
#     for j in range(1,9):
#         print(i*j)


#20. Print the first 10 natural numbers using loop:
# for i in range(1,11):
#     print("Natural number:",i)


#21. Python program to calculate the sum of all the odd numbers within the given range:

#22. Python program to calculate the sum of all the even numbers within the given range:
# for i in range(1,11):
    # if 


#23. Python program to count the space of a given string:
# a=input("Enter anythong: ")
# space=0
# for i in a:
#     if i.isspace():
#         space=space+1
#     else:
#         pass
# print("Number of spaces:",space)


#24. Pyhton program that accepts a string and calculate the number of digits,letters and space:
# a=input("Enter anything: ")
# digit=0
# letter=0
# space=0
# for i in a:
#     if i.isdigit():
#         digit=digit+1
#     elif i.isalpha():
#         letter=letter+1
#     elif i.isspace():
#         space=space+1
#     else:
#         pass
# print("Number of digits;",digit)
# print("Number of letters;",letter)
# print("Number of spaces;",space)
