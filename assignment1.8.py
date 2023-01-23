# TKINTER:
#1. Make Login and Registration page:

# Log in page:
# from tkinter import *
# win=Tk()

# win.title("Log In")

# win.minsize(width=300,height=300)
# win.maxsize(width=300,height=300)

# email=Label(win,text="Email: ").grid(row=0, column=0)
# e1=Entry(win).grid(row=0,column=1)
# password=Label(win,text="Password: ").grid(row=1, column=0)
# e2=Entry(win).grid(row=1, column=1)

# submit=Button(win,text="Submit").grid(row=4, column=1)

# win.mainloop()

# OR

# from tkinter import *
# root=Tk()

# root.title("Log In")
# root.configure(bg="light green")
# # #root.geometry("400x300")
# root.minsize(width=400, height=300)
# root.maxsize(width=400, height=300)

# from PIL import Image, ImageTk
# my_image=Image.open("dog.jpg")
# resize_image=my_image.resize((400,350))
# converted_image=ImageTk.PhotoImage(resize_image)
# my_label=Label(root, image=converted_image, width=400, height=380)
# my_label.pack()

# username=Label(root, text="Username: ").place(x=30, y=50)
# e1=Entry(root).place(x=120, y=50)
# email=Label(root, text="Email: ").place(x=30,y=90)
# e1=Entry(root).place(x=120, y=90)
# password=Label(root, text="Password: ").place(x=30,y=130)
# e2=Entry(root).place(x=120, y=130)

# def func():
#     print("Logged In")

# btn=Button(root, text="Login", command=func)
# btn.place(x=170, y=160)

# root.mainloop()


#2. if log in is clicked then print"Hello python" and if registration is clicked then print"Hello softwarica":
# from tkinter import *
# win=Tk()
# win.geometry('300x300')

# def func():
#     print("Hello Python")
# btn1=Button(win,text="Login", command=func)
# btn1.pack(side="top")

# def func():
#     print("Hello Softwarica")
# btn2=Button(win,text="Register", command=func)
# btn2.pack(side="top")

# win.mainloop()


#3. Registration page:
# from tkinter import *
# win=Tk()

# win.title("Sign Up")

# win.minsize(width=500,height=300)
# win.maxsize(width=500,height=300)

# win.configure(bg='light blue')

# f_name=Label(win,text="First Name: ").grid(row=0, column=0)
# e1=Entry(win).grid(row=0, column=1)
# l_name=Label(win,text="Last Name: ").grid(row=0, column=2)
# e2=Entry(win).grid(row=0, column=3)
# username=Label(win,text="Username: ").grid(row=1, column=0)
# e3=Entry(win).grid(row=1, column=1)
# email=Label(win,text="Email: ").grid(row=2, column=0)
# e4=Entry(win).grid(row=2, column=1)
# password=Label(win,text="Password: ").grid(row=3, column=0)
# e5=Entry(win).grid(row=3, column=1)
# confirm_pw=Label(win,text="Confirm Password: ").grid(row=4, column=0)
# e6=Entry(win).grid(row=4, column=1)

# check_value=IntVar
# check_box=Checkbutton(text="Remember me?", variable=check_value)
# check_box.grid(row=6, column=1)

# submit=Button(win, text="Submit").grid(row=8, column=1)

# win.mainloop()


#4. Make log in button and registration button:
# if log in is clicked then print"Hello python" and if registration is clicked then print"Hello softwarica":
# from tkinter import *
# win=Tk()
# win.geometry('300x300')
# def func():
#     print("Hello Python")

# btn1=Button(win,text="Login", command=func)
# btn1.pack(side="top")
# btn2=Button(win,text="Register", command=func)
# btn2.pack(side="top")

# win.mainloop()


#5. Creating buttons that prints a certain statement:
# from tkinter import *
# window=Tk()
# window.geometry('300x300')
# def myClick():
#     myLabel=Label(window, text="Look! I clicked a button", fg="dark blue",bg="light blue", font=50)
#     myLabel.pack()

# my_button= Button(window, text="Click me",padx=10,pady=10, command=myClick, fg="hotpink",bg="light pink")
# my_button.pack()
# window.mainloop()

#6. to disable the button:


#7. 
# from tkinter import *
# root=Tk()
# root.title("GUI")
# root.maxsize(width=600,height=300)
# root.minsize(width=600,height=300)

# #function:
# def add():
#     x=var.get()
#     print(x)
#     mylabell.config(text=x,bg="green")

# #label1
# mylabel=Label(root,text="User Name",fg="red",bg="yellow")
# mylabel.place(x=10,y=10)

# #label2
# mylabell=Label(root,text="Nothing",fg="red",bg="yellow")
# mylabell.place(x=40,y=120)

# #entry
# var=StringVar()
# ent=Entry(root,bg="white",fg="black",textvariable=var)
# ent.place(x=80,y=10)

# #button
# btn=Button(root,text="Submit",bg="green",fg="white",command=add)
# btn.place(x=20,y=80)

# root.bind('<Return>',lambda event:add())

# root.mainloop()


#8. from tkinter import *
# root=Tk()

# def click():
#     text1="Address: "+ mytext.get('1.0',END)
#     lbl.config(text=str(text1))

# mytext= Text(root, font=20, width=20, height=10)
# mytext.place(x=0, y=50)

# btn=Button(root, text="Click Me",font=30, command=click)
# btn.place(x=400,y=300)

# lbl=Label(root, text="", font=30)
# lbl.place(x=200, y=300)

# root.mainloop()


#9. Adding Frames to program:
# from tkinter import *
# window=Tk()
# frame=LabelFrame(window, text="This is my frame",padx=10,pady=10)
# frame.pack(padx=50, pady=50)
# b=Button(frame, text="Don't click here")
# b2=Button(frame, text=".....here")
# b.grid(row=0, column=0)
# b2.grid(row=1, column=1)
# window.mainloop()


#10. Radio Button:
# from tkinter import *
# window=Tk()
# def add():
#     print(var.get())

# var=IntVar()
# var1=Radiobutton(window, text=" Male", variable=var, value=1, command=add)
# var1.pack(anchor=W)
# var2=Radiobutton(window, text="Female", variable=var, value=2, command=add)
# var2.pack(anchor=W)

# window.mainloop()


#11. Adding buttons with command:
# from tkinter import *
# window=Tk()
# def add():
#     selection="you have selected the option"+str(var.get())
#     label.config(text=selection)

# var=IntVar()
# r1=Radiobutton(window, text="Option 1", variable=var, value=1, command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window, text="Option 2", variable=var, value=2, command=add)
# r2.pack(anchor=W)
# r3=Radiobutton(window, text="Option 3", variable=var, value=3, command=add)
# r3.pack(anchor=W)
# label=Label(window)
# label.pack()

# window.mainloop()


#12. Adding music check box:
# to import message box:
# from tkinter import *
# top=Tk()
# def add():
#     label.config(text=CheckVar.get())
# CheckVar1=IntVar()

# C1=Checkbutton(top, text="Music", variable=CheckVar1, \
#                 onvalue=1, offvalue=0, height=5, \
#                     width=20
#                     )

# C1.pack()
# btn=Button(top, text="Click", command=add)
# label=Label(top, text="")
# label.pack()
# btn.pack()

# top.mainloop()


# install pip
# pip install pillow

#13. Images as background:
# from tkinter import *
# from PIL import Image, ImageTk
# window=Tk()
# window.title("Log In")

# # define image
# my_image=ImageTk.PhotoImage(Image.open("images.jpeg"))

# # create a label
# my_label=Label(image=my_image)
# my_label.pack()

# # Button quit option
# button_quit=Button(window, text="Exit", command=window.quit, width=20)
# button_quit.pack()
# window.mainloop()


#14. registration page
# from tkinter import *
# root=Tk()

# root.maxsize(width=500, height=300)
# root.minsize(width=500, height=300)

# root.configure(bg="light green")

# root.title("Sign Up")

# def register_value():
#     print("successfully saved")

# # Label(root, text="Python Registration Form",).grid(row=0,column=4)

# fname_user = Label(root, text="First Name: ")
# fname_user.grid(row=1, column=2)
# lname_user = Label(root, text="Last Name: ")
# lname_user.grid(row=1, column=4)
# branch_user = Label(root, text="Branch: ")
# branch_user.grid(row=2, column=2)
# gender_user = Label(root, text="Gender: ")
# gender_user.grid(row=3, column=2)
# phone_user =Label(root, text="Contact no.: ")
# phone_user.grid(row=4, column=2)
# country_user = Label(root, text="Country: ")
# country_user.grid(row=5, column=2)

# fname_value = StringVar
# lname_value = StringVar
# branch_value = StringVar
# gender_value = StringVar
# phone_value = StringVar
# country_value = StringVar
# check_value = IntVar

# fname_box = Entry(root, textvariable = fname_value)
# fname_box.grid(row=1, column=3)
# lname_box = Entry(root, textvariable = lname_value)
# lname_box.grid(row=1, column=5)
# branch_box = Entry(root, textvariable = branch_value)
# branch_box.grid(row=2, column=3)
# gender_box = Entry(root, textvariable = gender_value)
# gender_box.grid(row=3, column=3)
# phone_box = Entry(root, textvariable = phone_value)
# phone_box.grid(row=4, column=3)
# country_box = Entry(root, textvariable = country_value)
# country_box.grid(row=5, column=3)
# check_box=Checkbutton(root, text="Remember me?", variable=check_value)
# check_box.grid(row=6, column=3)

# register_values=Button(root, text="Register").grid(row=8, column=4)

# root.mainloop()


# Adding message box:
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox

# root=Tk()
# root.title("Message Box")
# # root.iconbitmap('images.jpeg')

# def popup():
#     #showinfo messagebox:
#     messagebox.showinfo("This is my Popup","Hello World!")


# Button(root, text="Popup", command=popup).pack()

# mainloop()


# Try ALL:
# showinfo, showwarning, showerror, askquestions, askokcancel, askyesno

# Creating new windows:
# from tkinter import *
# from PIL import Image, ImageTk
# root=Tk()
# def open():
#     global my_img
#     top=Toplevel()
#     my_img=ImageTk.PhotoImage(Image.open("images.jpeg"))
#     my_label=Label(top,image=my_img)
#     my_label.pack(pady=10)
#     btn=Button(top, text="Close Window", command=top.destry)
#     btn.pack()

# btnn=Button(root, text="Open", command=open)
# btnn.pack()
# root.mainloop()


# Dropdown menu:
# from tkinter import*
# root=Tk()
# root.geometry("200x200")
# def show():
#     label.config(text= clicked.get() )
# # drop down menu options
# options=[
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday"
# ]
# clicked=StringVar()
# clicked.set("Monday")

# drop=OptionMenu(root,clicked, *options)
# drop.pack()

# button = Button(root, text="click me", command= show).pack()

# label=Label(root, text=" ")
# label.pack()

# root.mainloop()


# make login and regisrration page:
# make prototype with low fedelity and high fedelity:
# balsamig
# figma and canva


# Make a simple calculator:
# from tkinter import *
# root=Tk()
# root.title("Simple Calculator")
# e=Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# def button_click(number):
#     current=e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + str(number))

# def button_clear():
#     e.delete(0, END)

# def button_add():
#     first_number=e.get()
#     global f_num 
#     f_num=int(first_number)
#     e.delete(0, END)

# def button_sub():
#     first_number=e.get()
#     global f_num 
#     f_num=int(first_number)
#     e.delete(0, END)

# def button_mul():
#     first_number=e.get()
#     global f_num 
#     f_num=int(first_number)
#     e.delete(0, END)

# def button_div():
#     first_number=e.get()
#     global f_num 
#     f_num=int(first_number)
#     e.delete(0, END)

# def button_equal():
#     second_number=e.get()
#     e.delete(0, END)
#     e.insert(0, f_num + int(second_number)) 
#     e.insert(0, f_num - int(second_number))
#     e.insert(0, f_num * int(second_number)) 
#     e.insert(0, f_num / int(second_number)) 

# # Defining the buttons
# button_1=Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
# button_2=Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
# button_3=Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
# button_4=Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
# button_5=Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
# button_6=Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
# button_7=Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
# button_8=Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
# button_9=Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
# button_0=Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
# button_add=Button(root, text="+", padx=40, pady=20, command= button_add)
# button_sub=Button(root, text="-", padx=40, pady=20, command= button_sub)
# button_mul=Button(root, text="x", padx=40, pady=20, command= button_mul)
# button_div=Button(root, text="/", padx=40, pady=20, command= button_div)
# button_equal=Button(root, text="=", padx=91, pady=20, command=button_equal)
# button_clear=Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# # Putting buttons on the screen:
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)

# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)

# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)

# button_0.grid(row=4, column=0)
# button_add.grid(row=5, column=0)
# button_sub.grid(row=6, column=0)
# button_mul.grid(row=6, column=1)
# button_div.grid(row=6, column=2)
# button_clear.grid(row=4, column=1, columnspan=2)
# button_equal.grid(row=5, column=1, columnspan=2)

# root.mainloop()