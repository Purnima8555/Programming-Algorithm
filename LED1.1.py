# LOG IN PAGE:
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image,ImageTk
# import ast

# root=Tk()
# root.title('Login')
# root.geometry('800x400+200+200')
# root.configure(bg="white")
# root.resizable(False, False)

# def signin():
#     username=user.get()
#     password=code.get()

#     if username=='admin' and password=='1234':
#         screen=Toplevel(root)
#         screen.title("App")
#         screen.geometry('925x500+300+200')
#         screen.config(bg="white")

#         Label(screen, text="Hello Everyone!", bg='white', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

#         screen.mainloop()

#     elif username!='admin' and password!='1234':
#         messagebox.showerror("Error","Invalid username and password")

#     elif password!="1234":
#         messagebox.showerror("Error","Invalid password")

#     elif username!="admin":
#         messagebox.showerror("Error","Invalid Username")



# frame1=Frame(root,width=400, height=400, bg="blue")
# frame1.place(x=80, y=80)
# image=(Image.open("task-mng.webp"))
# resize_image=image.resize((300,310))
# imagess=ImageTk.PhotoImage(resize_image)
# lbl=Label(frame1, image=imagess, width=200, height=200)
# lbl.pack()
  
# frame=Frame(root, width=350, height=390, bg='white')
# frame.place(x=400, y=50)

# heading=Label(frame, text='Log In', fg="black", font=('Officina',23,'bold'))
# heading.place(x=130, y=1)

# ############-------------------
# def on_enter(e):
#     user.delete(0, 'end')

# def on_leave(e):
#     name=user.get()
#     if name=='':
#         user.insert(0, 'Username')

# user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# user.place(x=30, y=80)
# user.insert(0,'Username')
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ############--------------------
# def on_enter(e):
#     code.delete(0, 'end')

# def on_leave(e):
#     name=code.get()
#     if name=='':
#         code.insert(0, 'Password')

# code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# code.place(x=30, y=150)
# code.insert(0, 'Password')
# code.bind('<FocusIn>', on_enter)
# code.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# ############---------------------
# Button(frame, width=39, pady=7, text='Login', bg='lime green', fg='white', border=0, command=signin).place(x=35, y=204)
# label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
# label.place(x=100, y=270)

# sign_up=Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='lime green')
# sign_up.place(x=220, y=270)

# root.bind('<Return>',lambda event:signin())

# root.mainloop()


# REGISTRATION PAGE:
# from tkinter import *
# from tkinter import messagebox
# import ast

# root=Tk()
# root.title('Sign Up')
# root.geometry('800x400+200+200')
# root.configure(bg="white")
# root.resizable(False, False)

# def signin():
#     username=user.get()
#     password=code.get()

#     if username=='admin' and password=='1234':
#         screen=Toplevel(root)
#         screen.title("App")
#         screen.geometry('925x500+300+200')
#         screen.config(bg="white")

#         Label(screen, text="Hello Everyone!", bg='white', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

#         screen.mainloop()

#     elif username!='admin' and password!='1234':
#         messagebox.showerror("Error","Invalid username and password")

#     elif password!="1234":
#         messagebox.showerror("Error","Invalid password")

#     elif username!="admin":
#         messagebox.showerror("Error","Invalid Username")


# frame=Frame(root, width=370, height=380, bg='blue')
# frame.place(x=50, y=10)

# heading=Label(frame, text='Register', fg="black", font=('Officina',23,'bold'))
# heading.place(x=130, y=1)

# ############-------------------
# def on_enter(e):
#     fname.delete(0, 'end')

# def on_leave(e):
#     name=fname.get()
#     if name=='':
#         fname.insert(0, 'First Name')

# fname=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# fname.place(x=30, y=82)
# fname.insert(0,'First Name')
# fname.bind('<FocusIn>', on_enter)
# fname.bind('<FocusOut>', on_leave)

# Frame(frame, width=135, height=2, bg='black').place(x=25, y=107)

# ############-------------------
# def on_enter(e):
#     lname.delete(0, 'end')

# def on_leave(e):
#     name=lname.get()
#     if name=='':
#         lname.insert(0, 'Last Name')

# lname=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# lname.place(x=190, y=82)
# lname.insert(0,'Last Name')
# lname.bind('<FocusIn>', on_enter)
# lname.bind('<FocusOut>', on_leave)

# Frame(frame, width=138, height=2, bg='black').place(x=180, y=107)

# ############-------------------
# def on_enter(e):
#     user.delete(0, 'end')

# def on_leave(e):
#     name=user.get()
#     if name=='':
#         user.insert(0, 'Username')

# user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# user.place(x=30, y=124)
# user.insert(0,'Username')
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=149)

# ############-------------------
# def on_enter(e):
#     email.delete(0, 'end')

# def on_leave(e):
#     name=email.get()
#     if name=='':
#         email.insert(0, 'Email address')

# email=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# email.place(x=30, y=166)
# email.insert(0, 'Email address')
# email.bind('<FocusIn>', on_enter)
# email.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=191)

# ############--------------------
# def on_enter(e):
#     code.delete(0, 'end')

# def on_leave(e):
#     name=code.get()
#     if name=='':
#         code.insert(0, 'Password')

# code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# code.place(x=30, y=208)
# code.insert(0, 'Password')
# code.bind('<FocusIn>', on_enter)
# code.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=233)

# ############--------------------
# check_value=IntVar
# check_box=Checkbutton(text="I read and agree to Terms & Conditions?",fg='black',font=('Officina',7), variable=check_value)
# check_box.place(x=90, y=250)

# ############--------------------
# Button(frame, width=39, pady=7, text='Register', bg='lime green', fg='white', border=0, command=signin).place(x=35, y=274)
# label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
# label.place(x=100, y=320)

# sign_up=Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='lime green')
# sign_up.place(x=220, y=320)

# root.bind('<Return>',lambda event:signin())

# root.mainloop()


# # To use image in tkinter:
# # from tkinter import *
# # from PIL import Image,ImageTk

# # root=Tk()
# # image=ImageTk.PhotoImage(Image.open("a.png"))
# # lbl=Label(root,image=image)
# # lbl.pack()
# # root.mainloop()









# LOG IN PAGE:

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image,ImageTk
# import ast

# root=Tk()
# root.title('Login')
# root.geometry('800x400+200+200')
# root.configure(bg="white")
# root.resizable(False, False)

# ############-------------------
# def signin():
#     username=user.get()
#     password=code.get()

#     if username=='admin' and password=='1234':
#         screen=Toplevel(root)
#         screen.title("App")
#         screen.geometry('925x500+300+200')
#         screen.config(bg="white")

#         Label(screen, text="Hello Everyone!", bg='white', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

#         screen.mainloop()

#     elif username!='admin' and password!='1234':
#         messagebox.showerror("Error","Invalid username and password")

#     elif password!="1234":
#         messagebox.showerror("Error","Invalid password")

#     elif username!="admin":
#         messagebox.showerror("Error","Invalid Username")


# ############-------------------
# frame1=Frame(root,width=350, height=300, bg="blue")
# frame1.place(x=60, y=40)
# image=(Image.open("task-mng.webp"))
# resize_image=image.resize((310,330))
# imagess=ImageTk.PhotoImage(resize_image)
# lbl=Label(frame1, image=imagess, width=300, height=300)
# lbl.pack()
  
# frame=Frame(root, width=350, height=390, bg='white')
# frame.place(x=400, y=50)

# heading=Label(frame, text='Log In', fg="#917991", font=('Officina',23,'bold'))
# heading.place(x=130, y=1)

# ############-------------------
# def on_enter(e):
#     user.delete(0, 'end')

# def on_leave(e):
#     name=user.get()
#     if name=='':
#         user.insert(0, 'Username')

# user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# user.place(x=30, y=80)
# user.insert(0,'Username')
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ############--------------------
# def on_enter(e):
#     code.delete(0, 'end')

# def on_leave(e):
#     name=code.get()
#     if name=='':
#         code.insert(0, 'Password')

# code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# code.place(x=30, y=150)
# code.insert(0, 'Password')
# code.bind('<FocusIn>', on_enter)
# code.bind('<FocusOut>', on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# ############---------------------
# Button(frame, width=39, pady=7, text='Login', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=204)
# label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Officina',8))
# label.place(x=100, y=270)

# sign_up=Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#917991')
# sign_up.place(x=220, y=270)

# root.bind('<Return>',lambda event:signin())

# root.mainloop()






# REGISTRATION PAGE:

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image,ImageTk
# import ast

# root=Tk()
# root.title('Sign Up')
# root.geometry('800x400+200+200')
# root.configure(bg="white")
# root.resizable(False, False)

# def signin():
#     first_name=fname.get()
#     last_name=lname.get()
#     email=email.get()
#     username=user.get()
#     password=code.get()
#     confirm_password=confirm_code.get()

#     if password==confirm_password:
#         try:
#             file=open('datasheet.txt','r+')
#             d=file.read()
#             r=ast.literal_eval(d)

#             dict2={username:password}
#             r.update(dict2)
#             file.truncate(0)
#             file.close()

#             file=open('datasheet.txt','w')
#             w=file.write(str(r))

#             messagebox.showinfo('Sign Up','Successfully sign up')

#         except:
#             file=open('datasheet.txt','w')
#             pp=str({'Username':'password'})
#             file.write(pp)
#             file.close()

#     else:
#         messagebox.showerror('Invalid',"Both Password should match")


# ############-------------------
# frame1=Frame(root,width=350, height=300, bg="blue")
# frame1.place(x=400, y=30)
# image=(Image.open("reg-mng.jpg"))
# resize_image=image.resize((400,400))
# imagess=ImageTk.PhotoImage(resize_image)
# lbl=Label(frame1, image=imagess, width=400, height=400)
# lbl.pack()

# frame=Frame(root, width=370, height=380, bg='white')
# frame.place(x=50, y=10)

# heading=Label(frame, text='Register', fg="#917991", font=('Officina',23,'bold'))
# heading.place(x=130, y=1)

# ############-------------------
# def on_enter(e):
#     fname.delete(0, 'end')

# def on_leave(e):
#     name=fname.get()
#     if name=='':
#         fname.insert(0, 'First Name')

# fname=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# fname.place(x=30, y=82)
# fname.insert(0,'First Name')
# fname.bind('<FocusIn>', on_enter)
# fname.bind('<FocusOut>', on_leave)

# Frame(frame, width=145, height=2, bg='black').place(x=25, y=107)

# ############-------------------
# def on_enter(e):
#     lname.delete(0, 'end')

# def on_leave(e):
#     name=lname.get()
#     if name=='':
#         lname.insert(0, 'Last Name')

# lname=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# lname.place(x=190, y=82)
# lname.insert(0,'Last Name')
# lname.bind('<FocusIn>', on_enter)
# lname.bind('<FocusOut>', on_leave)

# Frame(frame, width=154, height=2, bg='black').place(x=180, y=107)

# ############-------------------
# def on_enter(e):
#     user.delete(0, 'end')

# def on_leave(e):
#     name=user.get()
#     if name=='':
#         user.insert(0, 'Username')

# user=Entry(frame, width=25, fg='black', border=0, bg='white', font=('Officina',11))
# user.place(x=30, y=124)
# user.insert(0,'Username')
# user.bind('<FocusIn>', on_enter)
# user.bind('<FocusOut>', on_leave)

# Frame(frame, width=310, height=2, bg='black').place(x=25, y=149)

# ############-------------------
# def on_enter(e):
#     email.delete(0, 'end')

# def on_leave(e):
#     name=email.get()
#     if name=='':
#         email.insert(0, 'Email address')

# email=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# email.place(x=30, y=166)
# email.insert(0, 'Email address')
# email.bind('<FocusIn>', on_enter)
# email.bind('<FocusOut>', on_leave)

# Frame(frame, width=310, height=2, bg='black').place(x=25, y=191)

# ############--------------------
# def on_enter(e):
#     code.delete(0, 'end')

# def on_leave(e):
#     name=code.get()
#     if name=='':
#         code.insert(0, 'Password')

# code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# code.place(x=30, y=208)
# code.insert(0, 'Password')
# code.bind('<FocusIn>', on_enter)
# code.bind('<FocusOut>', on_leave)

# Frame(frame, width=310, height=2, bg='black').place(x=25, y=233)

# ##------------------------------
# def on_enter(e):
#     confirm_code.delete(0, 'end')

# def on_leave(e):
#     name=confirm_code.get()
#     if name=='':
#         confirm_code.insert(0, 'Confirm Password')

# confirm_code=Entry(frame, width=25, fg='black', border=0, bg="white", font=('Officina',11))
# confirm_code.place(x=30, y=250)
# confirm_code.insert(0, 'Confirm Password')
# confirm_code.bind('<FocusIn>', on_enter)
# confirm_code.bind('<FocusOut>', on_leave)

# Frame(frame, width=310, height=2, bg='black').place(x=25, y=275)

# ############--------------------
# check_value=IntVar
# check_box=Checkbutton(text="I read and agree to Terms & Conditions?",fg='black',font=('Officina',7), variable=check_value)
# check_box.place(x=90, y=290)

# ############--------------------
# Button(frame, width=39, pady=7, text='Register', bg='#917991', fg='white', border=0, command=signin).place(x=35, y=305)
# label=Label(frame, text="Already have an account?", fg='black', bg='white', font=('Officina',8))
# label.place(x=100, y=344)

# sign_up=Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#917991')
# sign_up.place(x=231, y=344)

# root.bind('<Return>',lambda event:signin())

# root.mainloop()




# TO DO LIST:

# 1.
# from tkinter import *
# from tkinter import messagebox

# def newTask():
#     task = my_entry.get()
#     if task != "":
#         lb.insert(END, task)
#         my_entry.delete(0, "end")
#     else:
#         messagebox.showwarning("warning", "Please enter some task.")

# def deleteTask():
#     lb.delete(ANCHOR)
    
# ws = Tk()
# ws.geometry('500x450+500+200')
# ws.title('PythonGuides')
# ws.config(bg='#223441')
# ws.resizable(width=False, height=False)

# frame = Frame(ws)
# frame.pack(pady=10)

# lb = Listbox(
#     frame,
#     width=25,
#     height=8,
#     font=('Times', 18),
#     bd=0,
#     fg='#464646',
#     highlightthickness=0,
#     selectbackground='#a6a6a6',
#     activestyle="none",
    
# )
# lb.pack(side=LEFT, fill=BOTH)

# task_list = [
#     'Eat apple',
#     'drink water',
#     'go gym',
#     'write software',
#     'write documentation',
#     'take a nap',
#     'Learn something',
#     'paint canvas'
#     ]

# for item in task_list:
#     lb.insert(END, item)

# sb = Scrollbar(frame)
# sb.pack(side=RIGHT, fill=BOTH)

# lb.config(yscrollcommand=sb.set)
# sb.config(command=lb.yview)

# my_entry = Entry(
#     ws,
#     font=('times', 24)
#     )

# my_entry.pack(pady=20)

# button_frame = Frame(ws)
# button_frame.pack(pady=20)

# addTask_btn = Button(
#     button_frame,
#     text='Add Task',
#     font=('times 14'),
#     bg='#c5f776',
#     padx=20,
#     pady=10,
#     command=newTask
# )
# addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# delTask_btn = Button(
#     button_frame,
#     text='Delete Task',
#     font=('times 14'),
#     bg='#ff8b61',
#     padx=20,
#     pady=10,
#     command=deleteTask
# )
# delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


# ws.mainloop()



# 2.
# import tkinter as tk                    # importing the tkinter module as tk  
# from tkinter import ttk                 # importing the ttk module from the tkinter library  
# from tkinter import messagebox          # importing the messagebox module from the tkinter library  
# import sqlite3 as sql                   # importing the sqlite3 module as sql  
  
# # defining the function to add tasks to the list  
# def add_task():  
#     # getting the string from the entry field  
#     task_string = task_field.get()  
#     # checking whether the string is empty or not  
#     if len(task_string) == 0:  
#         # displaying a message box with 'Empty Field' message  
#         messagebox.showinfo('Error', 'Field is Empty.')  
#     else:  
#         # adding the string to the tasks list  
#         tasks.append(task_string)  
#         # using the execute() method to execute a SQL statement  
#         the_cursor.execute('insert into tasks values (?)', (task_string ,))  
#         # calling the function to update the list  
#         list_update()  
#         # deleting the entry in the entry field  
#         task_field.delete(0, 'end')  
  
# # defining the function to update the list  
# def list_update():  
#     # calling the function to clear the list  
#     clear_list()  
#     # iterating through the strings in the list  
#     for task in tasks:  
#         # using the insert() method to insert the tasks in the list box  
#         task_listbox.insert('end', task)  
  
# # defining the function to delete a task from the list  
# def delete_task():  
#     # using the try-except method  
#     try:  
#         # getting the selected entry from the list box  
#         the_value = task_listbox.get(task_listbox.curselection())  
#         # checking if the stored value is present in the tasks list  
#         if the_value in tasks:  
#             # removing the task from the list  
#             tasks.remove(the_value)  
#             # calling the function to update the list  
#             list_update()  
#             # using the execute() method to execute a SQL statement  
#             the_cursor.execute('delete from tasks where title = ?', (the_value,))  
#     except:  
#         # displaying the message box with 'No Item Selected' message for an exception  
#         messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# # function to delete all tasks from the list  
# def delete_all_tasks():  
#     # displaying a message box to ask user for confirmation  
#     message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
#     # if the value turns to be True  
#     if message_box == True:  
#         # using while loop to iterate through the tasks list until it's empty   
#         while(len(tasks) != 0):  
#             # using the pop() method to pop out the elements from the list  
#             tasks.pop()  
#         # using the execute() method to execute a SQL statement  
#         the_cursor.execute('delete from tasks')  
#         # calling the function to update the list  
#         list_update()  
  
# # function to clear the list  
# def clear_list():  
#     # using the delete method to delete all entries from the list box  
#     task_listbox.delete(0, 'end')  
  
# # function to close the application  
# def close():  
#     # printing the elements from the tasks list  
#     print(tasks)  
#     # using the destroy() method to close the application  
#     guiWindow.destroy()  
  
# # function to retrieve data from the database  
# def retrieve_database():  
#     # using the while loop to iterate through the elements in the tasks list  
#     while(len(tasks) != 0):  
#         # using the pop() method to pop out the elements from the list  
#         tasks.pop()  
#     # iterating through the rows in the database table  
#     for row in the_cursor.execute('select title from tasks'):  
#         # using the append() method to insert the titles from the table in the list  
#         tasks.append(row[0])  
  
# # main function  
# if __name__ == "__main__":  
#     # creating an object of the Tk() class  
#     guiWindow = tk.Tk()  
#     # setting the title of the window  
#     guiWindow.title("To-Do List Manager - JAVATPOINT")  
#     # setting the geometry of the window  
#     guiWindow.geometry("500x450+750+250")  
#     # disabling the resizable option  
#     guiWindow.resizable(0, 0)  
#     # setting the background color to #FAEBD7  
#     guiWindow.configure(bg = "#FAEBD7")  
  
#     # using the connect() method to connect to the database  
#     the_connection = sql.connect('listOfTasks.db')  
#     # creating the cursor object of the cursor class  
#     the_cursor = the_connection.cursor()  
#     # using the execute() method to execute a SQL statement  
#     the_cursor.execute('create table if not exists tasks (title text)')  
  
#     # defining an empty list  
#     tasks = []  
      
#     # defining frames using the tk.Frame() widget  
#     header_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
#     functions_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
#     listbox_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
  
#     # using the pack() method to place the frames in the application  
#     header_frame.pack(fill = "both")  
#     functions_frame.pack(side = "left", expand = True, fill = "both")  
#     listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
#     # defining a label using the ttk.Label() widget  
#     header_label = ttk.Label(  
#         header_frame,  
#         text = "The To-Do List",  
#         font = ("Brush Script MT", "30"),  
#         background = "#FAEBD7",  
#         foreground = "#8B4513"  
#     )  
#     # using the pack() method to place the label in the application  
#     header_label.pack(padx = 20, pady = 20)  
  
#     # defining another label using the ttk.Label() widget  
#     task_label = ttk.Label(  
#         functions_frame,  
#         text = "Enter the Task:",  
#         font = ("Consolas", "11", "bold"),  
#         background = "#FAEBD7",  
#         foreground = "#000000"  
#     )  
#     # using the place() method to place the label in the application  
#     task_label.place(x = 30, y = 40)  
      
#     # defining an entry field using the ttk.Entry() widget  
#     task_field = ttk.Entry(  
#         functions_frame,  
#         font = ("Consolas", "12"),  
#         width = 18,  
#         background = "#FFF8DC",  
#         foreground = "#A52A2A"  
#     )  
#     # using the place() method to place the entry field in the application  
#     task_field.place(x = 30, y = 80)  
  
#     # adding buttons to the application using the ttk.Button() widget  
#     add_button = ttk.Button(  
#         functions_frame,  
#         text = "Add Task",  
#         width = 24,  
#         command = add_task  
#     )  
#     del_button = ttk.Button(  
#         functions_frame,  
#         text = "Delete Task",  
#         width = 24,  
#         command = delete_task  
#     )  
#     del_all_button = ttk.Button(  
#         functions_frame,  
#         text = "Delete All Tasks",  
#         width = 24,  
#         command = delete_all_tasks  
#     )  
#     exit_button = ttk.Button(  
#         functions_frame,  
#         text = "Exit",  
#         width = 24,  
#         command = close  
#     )  
#     # using the place() method to set the position of the buttons in the application  
#     add_button.place(x = 30, y = 120)  
#     del_button.place(x = 30, y = 160)  
#     del_all_button.place(x = 30, y = 200)  
#     exit_button.place(x = 30, y = 240)  
  
#     # defining a list box using the tk.Listbox() widget  
#     task_listbox = tk.Listbox(  
#         listbox_frame,  
#         width = 26,  
#         height = 13,  
#         selectmode = 'SINGLE',  
#         background = "#FFFFFF",  
#         foreground = "#000000",  
#         selectbackground = "#CD853F",  
#         selectforeground = "#FFFFFF"  
#     )  
#     # using the place() method to place the list box in the application  
#     task_listbox.place(x = 10, y = 20)  
  
#     # calling some functions  
#     retrieve_database()  
#     list_update()  
#     # using the mainloop() method to run the application  
#     guiWindow.mainloop()  
#     # establishing the connection with database  
#     the_connection.commit()  
#     the_cursor.close()  


#     # Facebook:
#     # User table
#     # - Attributes
#     # - Last Name
#     # - Address
#     # - Email
#     # - Password

#     # Softwarica:



#     import tkinter as tk   
# from tkinter import ttk
# from tkinter import messagebox
# import sqlite3 as sql                 

# def add_task():  
      
#     task_string = task_field.get()  
      
#     if len(task_string) == 0:  

#         messagebox.showinfo('Error', 'Field is Empty.')  
#     else:  
          
#         tasks.append(task_string)  
         
#         the_cursor.execute('insert into tasks values (?)', (task_string ,))  
         
#         list_update()  
          
#         task_field.delete(0, 'end')  
  
  
# def list_update():  
     
#     clear_list()  
    
#     for task in tasks:  
          
#         task_listbox.insert('end', task)  
  
 
# def delete_task():  
      
#     try:  
          
#         the_value = task_listbox.get(task_listbox.curselection())  
          
#         if the_value in tasks:  
              
#             tasks.remove(the_value)  
              
#             list_update()  
              
#             the_cursor.execute('delete from tasks where title = ?', (the_value,))  
#     except:  
          
#         messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
  
# def delete_all_tasks():  
      
#     message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
      
#     if message_box == True:  
          
#         while(len(tasks) != 0):  
             
#             tasks.pop()  
          
#         the_cursor.execute('delete from tasks')  
          
#         list_update()  
  
  
# def clear_list():  
    
#     task_listbox.delete(0, 'end')  
  
  
# def close():  
    
#     print(tasks)  
     
#     guiWindow.destroy()  
  
 
# def retrieve_database():  
    
#     while(len(tasks) != 0):  
        
#         tasks.pop()  
      
#     for row in the_cursor.execute('select title from tasks'):  
          
#         tasks.append(row[0])  
  
# # main function  
# if __name__ == "__main__":  
      
#     guiWindow = tk.Tk()  
    
#     guiWindow.title("To-Do List Manager")  
      
#     guiWindow.geometry("800x400+200+200")  
      
#     guiWindow.resizable(0, 0)  
      
#     guiWindow.configure(bg = "#917991")  
  
    
#     the_connection = sql.connect('listOfTasks.db')  
    
#     the_cursor = the_connection.cursor()  
      
#     the_cursor.execute('create table if not exists tasks (title text)')  
  
     
#     tasks = []  
      
    
#     header_frame = tk.Frame(guiWindow, bg = "#ffffff")  
#     functions_frame = tk.Frame(guiWindow, bg = "#ffffff")  
#     listbox_frame = tk.Frame(guiWindow, bg = "#ffffff")  
  
    
#     header_frame.pack(fill = "both")  
#     functions_frame.pack(side = "left", expand = True, fill = "both")  
#     listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
     
#     header_label = ttk.Label(  
#         header_frame,  
#         text = "The To-Do List",  
#         font = ("officina", "35"),  
#         background = "#917991",  
#         foreground = "#000000" ,
#     )  
     
#     header_label.pack(padx = 20, pady = 20)  
  
     
#     task_label = ttk.Label(  
#         functions_frame,  
#         text = "Enter the Task:",  
#         font = ("Consolas", "11", "bold"),  
#         background = "#917991",  
#         foreground = "#000000"  
#     )  
    
#     task_label.place(x = 30, y = 40)  
      
     
#     task_field = ttk.Entry(  
#         functions_frame,  
#         font = ("Consolas", "12"),  
#         width = 18,  
#         background = "#FFF8DC",  
#         foreground = "#A52A2A"  
#     )  
    
#     task_field.place(x = 30, y = 80)  
  
     
#     add_button = ttk.Button(  
#         functions_frame,  
#         text = "Add Task",  
#         width = 24,  
#         command = add_task  
#     )  
#     del_button = ttk.Button(  
#         functions_frame,  
#         text = "Delete Task",  
#         width = 24,  
#         command = delete_task  
#     )  
#     del_all_button = ttk.Button(  
#         functions_frame,  
#         text = "Delete All Tasks",  
#         width = 24,  
#         command = delete_all_tasks  
#     )  
#     exit_button = ttk.Button(  
#         functions_frame,  
#         text = "Exit",  
#         width = 24,  
#         command = close  
#     )  
      
#     add_button.place(x = 30, y = 120)  
#     del_button.place(x = 30, y = 160)  
#     del_all_button.place(x = 30, y = 200)  
#     exit_button.place(x = 30, y = 240)  
  
    
#     task_listbox = tk.Listbox(  
#         listbox_frame,  
#         width = 26,  
#         height = 13,  
#         selectmode = 'SINGLE',  
#         background = "#FFFFFF",  
#         foreground = "#000000",  
#         selectbackground = "#CD853F",  
#         selectforeground = "#FFFFFF"  
#     )  
     
#     task_listbox.place(x = 10, y = 20)  
  
     
#     retrieve_database()  
#     list_update()  
      
#     guiWindow.mainloop()  
   
#     the_connection.commit()  
#     the_cursor.close()  




