# 1. To print fibonacci number using while loop:
# n=int(input("Enter number: "))
# x=0
# y=1
# z=0
# while (z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y


# 2. Print 10 number of finonacci series using for loop:
# n=int(input("Enter number: "))
# i=int(n)
# x=0
# y=1
# z=0
# for i in n:
#     x=y
#     y=z
#     z=x+y
# print(z)


# 3. Fibonacci series using recursion:
# def a(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return a(n-1) + a(n-2)
# n=int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(a(i))


# 4. Factorial of a number using recursion:
# def fact(num):
#     """ This function call itself to find the factorial of a number """
#     if num==1:
#         return 1
#     else:
#         return(num*fact(num-1))
# num=int(input("Enter number: "))
# print("Factorial of",num,"is:", fact(num))


# 5. Reverse string using recursion:


# 6. Using recursion get the sum of natural number 10:
# def fact(num):
#     if num==1:
#         return 1
#     else:
#         return(num+fact(num-1))
# num=10
# print("Sum of", num, "natural number is:", fact(num))


# 7. To know the recursion limit and create a certain limit:
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(4000)
# print(sys.getrecursionlimit())


