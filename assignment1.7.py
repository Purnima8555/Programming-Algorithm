#1. write a python program to get the smallest number from a list:
# a=[1,2,3,4,5]
# a.sort()
# b=a.pop(0)
# print(b, "Is the smallest")


#2. write a python program to get the greatest number from a list:
# a=[1,2,3,4,5]
# a.sort()
# a.reverse()
# b=a.pop(0)
# print(b, "Is the greatest number")


#3. Write a python program to select an item randomly from a list:
# import random
# a= [1,2,3,4,5,6]
# print(random.choice(a))


#4. write a python program to copy a list:
# a=[1,2,3,4,5]
# b=a[:]
# print(b)


#5. write a python program to find the second largest number:
# a=[1,2,3,4,5]
# a.sort()
# a.reverse()
# b=a.pop(1)
# print(b," Is the second largest number")


#6. write a python program to print a specified list after removing the 3rd element:
# a=[1,2,3,4,5,6]
# del a[2]
# print(a)


#7. write a python program to count even and odd numbers from a series of number:
# a=[1,2,3,4,5,6,7,8]
# i=0
# b=len(a)
# evencount=0
# oddcount=0
# while i<b:
#     if a[i]%2==0:
#         evencount+=1
#     else:
#         oddcount+=1
#     i=i+1
# print(evencount)
# print(oddcount)


#8. write a program to add an item in a tuple:
# a=(1,2,4,5)
# b=list(a)
# b.append(8)
# print(tuple(b))


#9. write a python program to convert tuple to list:
# a=(1,2,3,4,5)
# print(list(a))


#10. write a python program to convert list to tuple:
# a=[1,2,3,4,5]
# print(tuple(a))


#11. write a python program to convert list of tuple into ditionary:
# a=[(1,2),(3,1)]
# print(dict(a))


#12. write a python script to add a key to a dictionary:
# a={0:10, 1:20}
# a[2]=20
# print(a)


#13. write a python script to concatenate following dictionaries to create a new one:
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# dict4={dict1,dict2,dict3}
# print(dict4)


#14. write a python script to check if a given key already exists in a dictionary. 
# a={0:10,1:20,3:40}
# if a.get(3)==None:
#     print("Key 3 is not present")
# else:
#     print("Key 3 is present")


#15. write a python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of key sample dictionary
# a={}
# b=0
# for i in range(1,16):
#     b=i
#     a[i]=b
# print(a)


#16. write a python script to merge two python dictionaries
# a={2:'Hi',4:'Hello'}
# b={'a':'Hi','b':'Hello'}
# print(a|b)


#17. Write a python problem to find the 3rd largest number in the list
# a=[4,6,7,9,10,1,2]
# a.sort()
# a.reverse()
# print(a[2])


#18. Write a Python program to create a set.
# list=[1,2,3,4,5]
# b=set(list)
# print(b)


#19. Write a Python program to add member(s) in a set.
# myset={1,2,3,"Hello"}
# b=[1,2,3,4,5]
# myset.update(b)
# print(myset)

# OR

# myset={1,2,3,"Hello"}
# myset.update([1,2,"Hello",5,6,7,8])
# print(myset)


#20. Write a Python program to remove item(s) from set
# myset={1,2,3,"Hello"}
# myset.remove(1)
# print(myset)

# OR

# myset={1,2,3,"Hello"}
# myset.discard("Hello")
# print(myset)


#21. Write a Python program to remove an item from a set if it is present in the set.
# myset={1,2,3,"Hello"}
# if "Hello" in myset:
#     myset.remove("Hello")
# print(myset)


#22. Write a Python program to create an intersection of sets.
# myset={1,2,3,"Hello"}
# yourset = {5,4,3,"Hello"}
# myset.intersection_update(yourset)
# print(myset)


#23. Write a Python script to check if a given key exists in a dictionary.
# a={2:'Hi',4:'Hello'}
# if 2 in a.keys():
#     print(2,"Exists in a ditionary")


#24. Write a Python script to check if a given values exists in a dictionary.
# a={2:'Hi',4:'Hello'}
# if 'Hi' in a.values():
#     print("Hi exists in ditionary")


# write a python problem to iterate over sets
# a={1,2,"Hello",3,"Why"}
# for i in a:
#     print(i)


# 13, 17, 21, 22