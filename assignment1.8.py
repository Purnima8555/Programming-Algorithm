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
# my_image=Image.open("images.jpeg")
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


#11. 
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


#12. 
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