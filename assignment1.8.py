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


# Registration page:
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


#2. Make log in button and registration button:
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


#3. Creating buttons that prints a certain statement:
# from tkinter import *
# window=Tk()
# window.geometry('300x300')
# def myClick():
#     myLabel=Label(window, text="Look! I clicked a button", fg="dark blue",bg="light blue", font=50)
#     myLabel.pack()

# my_button= Button(window, text="Click me",padx=10,pady=10, command=myClick, fg="hotpink",bg="light pink")
# my_button.pack()
# window.mainloop()

#4. to disable the button:


#5. 
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


# from tkinter import *
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


# Adding Frames to program:
# from tkinter import *
# window=Tk()
# frame=LabelFrame(window, text="This is my frame",padx=10,pady=10)
# frame.pack(padx=50, pady=50)
# b=Button(frame, text="Don't click here")
# b2=Button(frame, text=".....here")
# b.grid(row=0, column=0)
# b2.grid(row=1, column=1)
# window.mainloop()


# Radio Button:
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
