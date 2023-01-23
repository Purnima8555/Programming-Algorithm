# (incomplete)   #LED(CRUDE)
# from tkinter import *
# import sqlite3

# root=Tk()
# root.title('Database Address Book')

# # Databases:

# # Create a database or connect to:
# conn=sqlite3.connect('address_book.db')

# # Create cursor
# # cursor class is an instance using which you can invoke mehtods that execute SQlite Statements
# # Fetch data from the result sets of the quesries
# c=conn.cursor()

# # Create table:
# c.execute(""" CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
# )""")
# print("Table created successfully")

# #Create text boxes:
# f_name=Entry(root, width=30)
# f_name.grid(row=0, column=1, padx=20)

# l_name=Entry(root, width=30)
# l_name.grid(row=1, column=1)

# address=Entry(root, width=30)
# address.grid(row=2, column=1)

# city_label=Label(root, text="City")
# city_label.grid(row=3, column=0)

# state_label=Label(root, text="State")
# state_label.grid(row=4, column=0)

# zipcode_label=Label(root, text="Zip Code")
# zipcode_label.grid(row=5, column=1)

# submit_button=Button(root, text="Add records")


# conn.commit()
# conn.close()
# root.mainloop()





# CRUDE:

# from tkinter import *
# from tkinter import messagebox
# import sqlite3

# root =Tk()
# root.title("Database Address Book")

# # Databases

# # Create a database or connect to one
# conn=sqlite3.connect("address_book.db")


# # cursur creating
# # execute any query we entry in the box
# c=conn.cursor()

# # create table
# # c.execute(""" CREATE TABLE address(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text
# #           zipcode integer
# # )""")
# # print ("Table created successfully")
# # commit change

# def submit():
#     # clear the text boxes
#     f_name.delete(0,END)
#     l_name.delete(0,END)
#     address.delete(0,END)
#     city.delete(0,END)
#     state.delete(0,END)
#     zipcode.delete(0,END)

# # Create text boxes:
# f_name =Entry(root,width =30)
# f_name.grid(row=0,column=1,padx=20)

# l_name=Entry(root,width=30)
# l_name.grid(row=1,column=1)

# address=Entry(root,width=30)
# address.grid(row=2,column=1)

# city=Entry(root,width=30)
# city.grid(row=3,column=1)

# state=Entry(root,width=30)
# state.grid(row=3,column=1)

# zipcode=Entry(root,width=30)
# zipcode.grid(row=4,column=1)

# # Create textbox labels
# f_name_label = Label(root, text="First Name")
# f_name_label.grid(row=0, column=0)

# l_name_label =Label(root,text="Last Name")
# l_name_label.grid(row=1, column=0)

# address_label = Label(root,text="Address")
# address_label.grid(row=2, column=0)

# city_label =Label(root,text="City")
# city_label.grid(row=3,column=0)

# state_label= Label(root,text="State")
# state_label.grid(row=3, column=0)

# # Create submit button
# submit_btn =Button(root,text="Add Records", command=submit)
# submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# # commit change
# conn.commit()

# # close connection
# conn.close()

# def submit():
# # Create a database or connect to one:        
#         conn=sqlite3.connect('address_book.db')  

# # Create cursor:
#         c=conn.cursor()

# # Insert into table:
#         c.execute("INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
#                 'f_name':f_name.get(),
#                 'l_name':l_name.get(),
#                 'address':address.get(),
#                 'city':city.get(),
#                 'state':state.get(),
#                 'zipcode':zipcode.get()
# })

# # Showinfo messagebox:
#         messagebox.showinfo("Addressess","Inserted Successfully")

#         conn.commit()

#         conn.close()

# def query():
# # Create a databases or connect to one:        
#         conn=sqlite3.connect('address_book.db')
# # Create cursor:
#         c=conn.cursor()
# # Query of the database:
#         c.execute("SELECT *, oid FROM addresses")

#         records=c.fetchall()
#         print(records)

#         conn.commit()
#         conn.close()

# # Create query button:
# query_btn=Button(root, text="Show Records", command=query)
# query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# def query():
# # Create a databases or connect to a one:
#         conn=sqlite3.connect('address_book.db')

# # Create cursor:
#         c=conn.cursor()

# # Query of th database:
#         c.execute("SELECT*, oid FROM addresses")

#         records=c.fetchall()
#         print(records)

# # Loop through the results:
#         print_record=' '
#         for record in records:
#                 print_record += str(record[0]) + ' ' + str(record[6]) + "\n"

#         query_label=Label(root, tex=print_record)
#         query_label.grid(row=8, column=0, columnspan=2)

#         conn.commit()
#         conn.close()


# delete_box=Entry(root, width=30)
# delete_box.grid(row=9, column=1, pady=5)

# delete_box_label=Label(root, text="Delete ID")
# delete_box_label.grid(row=9, column=0, paddy=5)

# # Create a delete button:
# delete_btn=Button(root, text="Delete", command=delete)
# delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# def delete():
#         conn=sqlite3.connect('address_book.db')

#         c=conn.cursor()

#         c.execute("DELETE from address WHERE oid = " + delete_box.get())
#         print('Delete Successfully')

#         records=c.fetchall()

#         print_record=' '
#         for record in records:
#         # str(record[6]) added for displaying the id  
#                 print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' +str(record[6]) + "\n"

#         query_label=Label(root, text=print_record)
#         query_label.grid(row=11, column=0, columnspan=2)

#         conn.commit()
#         conn.close()

# # Creating an update function:
# def update():
#         # Create a databases or connect to one
#         conn=sqlite3.connect('address_book.db')

#         # Create cursor
#         c=conn.cursor()

#         record_id=delete_box.get()

#         c.execute("""UPDATE addresses SET
#                 first_name= :first,
#                 last_name= :last,
#                 address= :address,
#                 city= :city,
#                 state= :state,
#                 zipcode= :zipcode,
#                 WHERE oid= :oid""",
#                 {'first': f_name_editor.get(),
#                 'last': l_name_editor.get(),
#                 'address': address_editor.get(),
#                 'city': city_editor.grt(),
#                 'state': state_editor.get(),
#                 'zipcode': zipcode_editor.get(),
#                 'oid': record_id
                
#                 }
# )

# conn.commit()
# conn.close()

# # Destroying all the data and closing window
# editor.destroy()

# # Create edit function to update a record:
# def edit():

#         global editor

#         editor=Tk()
#         editor.title('Update Data')
#         # editor.iconbitmap('E:/images/global.ico')
#         editor.geometry('300x400')

#         # Create a databases or connect to one
#         conn=sqlite3.connect('address_book.db')

#         # Create cursor
#         c=conn.cursor()

#         record_id=delete_box.get()

#         # query of the database
#         c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

#         records=c.fetchall()
#         # print(records)

#         # Creating global variable for all text boxes


# root.mainloop()
# # Create a database or connect to one:






# from tkinter import *
# from tkinter import messagebox 
# import sqlite3
# win=Tk()
# win.title('Database Address Book')

# conn=sqlite3.connect('address_book.db')
# c=conn.cursor()

# # c.execute(""" CREATE TABLE addresses(
# #     first_name text,
# #     last_name text,
# #     address text,
# #     city text,
# #     state text,
# #     zipcode integer
# # )""")
# # print('Table created sucessfully')

   

# f_name=Entry(win,width=30)
# f_name.grid(row=0,column=1,padx=20)

# l_name=Entry(win,width=30)
# l_name.grid(row=1,column=1)

# address=Entry(win,width=30)
# address.grid(row=2, column=1)

# city=Entry(win,width=30)
# city.grid(row=3,column=1)

# state=Entry(win,width=30)
# state.grid(row=4, column=1)

# zipcode=Entry(win,width=30)
# zipcode.grid(row=5, column=1)

# f_name_label=Label(win,text="First Name")
# f_name_label.grid(row=0, column=0)

# l_name_label=Label(win,text="Last Name")
# l_name_label.grid(row=1, column=0)

# address_label=Label(win,text="Address")
# address_label.grid(row=2, column=0)

# city_label=Label(win,text="City")
# city_label.grid(row=3, column=0)

# state_label=Label(win,text="state")
# state_label.grid(row=4, column=0)

# zipcode_label=Label(win,text="zipcode")
# zipcode_label.grid(row=5, column=0)



# def submit():
#     conn=sqlite3.connect('address_book.db')
#     c=conn.cursor()
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
#         'f_name':f_name.get(),
#         'l_name':l_name.get(),
#         'address':address.get(),
#         'city':city.get(),
#         'state':state.get(),
#         'zipcode':zipcode.get()
#     })

#     messagebox.showinfo("Address", "Inserted Successfully")
#     conn.commit()
#     conn.close()
#     f_name.delete(0,END)
#     l_name.delete(0,END)
#     address.delete(0,END)
#     city.delete(0,END)
#     state.delete(0,END)
#     zipcode.delete(0,END)

# def query():
#     conn=sqlite3.connect('address_book.db')
#     c=conn.cursor()
#     c.execute("SELECT *,oid FROM addresses")
#     records=c.fetchall()
#     print(records)
#     conn.commit()
#     conn.close()
# query_btn = Button(win, text="Show Records", command=query)
# query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# def query():
#     conn=sqlite3.connect('address_book.db')
#     c=conn.cursor()
#     c.execute("SELECT *,oid FROM addresses")
#     records=c.fetchall()
#     print(records)
#     print_record=''
#     for record in records:
#         print_record+= str(record[0])+''+ str(record[1]) +' '+'\t'+str(record[6]) +"\n"

#     query_label=Label(win,text=print_record)
#     query_label.grid(row=8, column=0, columnspan=2)

#     conn.commit()
#     conn.close()



# def delete():
#     conn=sqlite3.connect('address_book.db')
#     c=conn.cursor()
#     c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
#     print('Delete Successfully')
    
#     conn.commit()
#     conn.close()

# delete_box=Entry(win,width=30)
# delete_box.grid(row=9,column=1,pady=5)

# delete_box_label=Label(win,text="Delete ID")
# delete_box_label.grid(row=9,column=0,pady=5)

# delete_btn=Button(win,text="Delete",command=delete)
# delete_btn.grid(row=10,column=0,columnspan=2, pady=10, padx=10, ipadx=120)

# def update():
#     conn=sqlite3.connect('address_boook.db')
#     c=conn.cursor()
#     record_id=delete_box.get()
#     c.execute("""UPDATE addresses SET
#         first_name=:first,
#         last_name=:last,
#         address=:address,
#         city=:city,
#         state=:state,
#         zipcode=:zipcode
#         WHERE oid=:oid""",
#         {'first': f_name_editor.get(), 
#         'last':l_name_editor.get(),
#         'address':address_editor.get(),
#         'city':city_editor.get(),
#         'state':state_editor.get(),
#         'zipcode':zipcode_editor.get(),
#         'oid':record_id

#         }
#     )
#     conn.commit()
#     conn.close()
#     editor.destroy()

# def edit():
#     global editor

#     editor=Tk()
#     editor.title('Update Data')
#     editor.geometry('300x480')
#     conn=sqlite3.connect('address_book.db') 
#     c=conn.cursor()
#     record_id=delete_box.get()
#     c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
#     records=c.fetchall()

#     global f_name_editor
#     global l_name_editor
#     global address_editor
#     global city_editor
#     global state_editor
#     global zipcode_editor

#     f_name_editor=Entry(editor,width=30)
#     f_name_editor.grid(row=0,column=1,padx=20, pady=(10,0))

#     l_name_editor=Entry(editor,width=30)
#     l_name_editor.grid(row=1,column=1)

#     address_editor=Entry(editor,width=30)
#     address_editor.grid(row=2, column=1)

#     city_editor=Entry(editor,width=30)
#     city_editor.grid(row=3,column=1)

#     state_editor=Entry(editor,width=30)
#     state_editor.grid(row=4, column=1)

#     zipcode_editor=Entry(editor,width=30)
#     zipcode_editor.grid(row=5, column=1)

#     f_name_label=Label(editor,text="First Name")
#     f_name_label.grid(row=0, column=0, padx=(10,0))

#     l_name_label=Label(editor,text="Last Name")
#     l_name_label.grid(row=1, column=0)

#     address_label=Label(editor,text="Address")
#     address_label.grid(row=2, column=0)

#     city_label=Label(editor,text="City")
#     city_label.grid(row=3, column=0)

#     state_label=Label(editor,text="state")
#     state_label.grid(row=4, column=0)

#     zipcode_label=Label(editor,text="zipcode")
#     zipcode_label.grid(row=5, column=0)

#     for record in records:
#         f_name_editor.insert(0, record[0])
#         l_name_editor.insert(0, record[1])
#         address_editor.insert(0, record[2])
#         city_editor.insert(0, record[3])
#         state_editor.insert(0, record[4])
#         zipcode_editor.insert(0, record[5])

#     edit_btn=Button(editor,text="SAVE",command=update)
#     edit_btn.grid(row=6, column=0,columnspan=2,pady=10,padx=10,ipadx=125)
    
#     conn.commit()
#     conn.close()

# submit_btn=Button(win,text="Add Record", command=submit)
# submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query_btn=Button(win, text="Show Records", command=query)
# query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# delete_btn=Button(win, text="Delete", command=delete)
# delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# edit_btn=Button(win, text="Update", command=edit)
# edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# conn.commit()
# conn.close()

# win.mainloop()



#     # Softwarica:


# from tkinter import*
# from tkinter import messagebox
# import sqlite3

# root=Tk()
# root.title('Softwarica Database Address Book')

# conn=sqlite3.connect('softwarica_database.db')
# c=conn.cursor()

# #Create table
# # c.execute("""CREATE TABLE addresses (
# #     username text,
# #     first_name text,
# #     last_name text,
# #     address text,
# #     age integer,
# #     slcpercentage integer,
# #     twelvepercent integer,
# #     phonenumber integer
# # )""")
# # print("Table created successfully")


# def submit():
#     #create a databases or connect to one
#     conn=sqlite3.connect('softwarica_database.db')

#     #create cursor
#     c=conn.cursor()
# #Insert into table
#     c.execute("INSERT INTO addresses VALUES (:username, :f_name, :l_name, :address, :age, :slcpercent, :twelvepercent, :phonenumber)",{
#         'username':username.get(),
#         'f_name':f_name.get(),
#         'l_name':l_name.get(),
#         'address':address.get(),
#         'age':age.get(),
#         'slcpercent':slcpercent.get(),
#         'twelvepercent':twelvepercent.get(),
#         'phonenumber':phonenumber.get()
#     })
# #showinfo messagebox
#     messagebox.showinfo("Addresses", "Inserted Sucessfully")

#     conn.commit()
#     conn.close()

# def query():
# #     #create a database or connect to one
#     conn=sqlite3.connect('softwarica_database.db')

# #     #Create cursor
#     c= conn.cursor()

# #     #query of the database
#     c.execute("Select*, oid FROM addresses")

#     records=c.fetchall()
#     print(records)

# #     #loop through the results
#     print_record=''
#     for record in records:
#         print_record+= str(record[0]) + ' '+ str(record[1])+ ' '+ '\t'+ str(record[8])+ "\n"

#     query_label= Label(root,text=print_record)
#     query_label.grid(row=11, column=0, columnspan=2)

#     conn.commit()
#     conn.close()

# def delete():
# #     #create database
#     conn= sqlite3.connect('softwarica_database.db')
    
# #     #create cursor
#     c= conn.cursor()

# #     #delete a record
#     c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
#     print('Deleted Successfully')

# #     #query of th database
#     # c.execute("SELECT *, oil FROM addresses")

#     # records=c.fetchall()

#     # print_record=''
#     # for record in records:
#     #     print_record+= str(record[0]) + ' '+ str(record[1])+ ' '+ '\t'+ str(record[6])+ "\n"

#     # query_label= Label(root, text=print_record)
#     # query_label.grid(row=13, column=0, columnspan=2)

#     conn.commit()

#     conn.close()

# # #create delete buttons
# delete_box= Entry(root, width=30)
# delete_box.grid(row=12, column=1,pady=5)

# delete_box_label=Label(root, text="Delete ID")
# delete_box_label.grid(row=12, column=0, pady=5)

# delete_btn= Button(root, text="Delete", command=delete)
# delete_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# def update():
#     conn=sqlite3.connect('softwarica_database.db')
#     c=conn.cursor()

#     record_id= delete_box.get()

#     c.execute("""UPDATE addresses SET
#         username = :user,
#         first_name = :first,
#         last_name = :last,
#         address = :address,
#         age = :age,
#         slcpercentage = :slcpercent,
#         twelvepercent = :twelvepercent,
#         phonenumber = :number
#         WHERE oid = :oid""",
#         {

#          'user': username_editor.get(),
#          'first': f_name_editor.get(),
#          'last': l_name_editor.get(),
#          'address': address_editor.get(),
#          'age':age_editor.get(),
#          'slcpercent': slcpercent_editor.get(),
#          'twelvepercent':twelvepercent_editor.get(),
#          'number': phonenumber_editor.get(),
#          'oid':record_id
#                 })
#     conn.commit()
#     conn.close()
#     editor.destroy()


# def edit():
#     global editor

#     editor= Tk()
#     editor.title('Update Data')

#     editor.geometry('300x480')

#     conn= sqlite3.connect('softwarica_database.db')

#     c=conn.cursor()

#     record_id= delete_box.get()

#     c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

#     records = c.fetchall()
#     print(records)

#     global username_editor
#     global f_name_editor
#     global l_name_editor
#     global address_editor
#     global age_editor
#     global slcpercent_editor
#     global twelvepercent_editor
#     global phonenumber_editor

#     #
#     username_editor=Entry(editor, width=30)
#     username_editor.grid(row=0 ,column=1, padx=20, pady=(10,0))

#     f_name_editor=Entry(editor, width=30)
#     f_name_editor.grid(row=1, column=1)

#     l_name_editor=Entry(editor,width=30)
#     l_name_editor.grid(row=2, column=1)

#     address_editor=Entry(editor, width=30)
#     address_editor.grid(row=3, column=1)

#     age_editor=Entry(editor, width=30)
#     age_editor.grid(row=4, column=1)

#     slcpercent_editor=Entry(editor, width=30)
#     slcpercent_editor.grid(row=5, column=1)

#     twelvepercent_editor=Entry(editor, width=30)
#     twelvepercent_editor.grid(row=6, column=1)

#     phonenumber_editor= Entry(editor, width=30)
#     phonenumber_editor.grid(row=7, column=1)

# #     #
#     username_label=Label(editor, text="Username")
#     username_label.grid(row=0, column=0)

#     f_name_label=Label(editor,text="First Name")
#     f_name_label.grid(row=1, column=0)

#     l_name_label=Label(editor,text="Last Name")
#     l_name_label.grid(row=2,column=0)

#     address_label=Label(editor,text="Address")
#     address_label.grid(row=3,column=0)

#     age_label=Label(editor, text="Age")
#     age_label.grid(row=4, column=0)

#     slcpercent_label=Label(editor, text="SLC Percentage")
#     slcpercent_label.grid(row=5, column=0)

#     twelvepercent_label=Label(editor, text="Twelve Percentage")
#     twelvepercent_label.grid(row=6,column=0)

#     phonenumber_label=Label(editor, text="Phone Number")
#     phonenumber_label.grid(row=7, column=0)

#     #loop through results
#     for record in records:
#         username_editor.insert(0, record[0])
#         f_name_editor.insert(0, record[1])
#         l_name_editor.insert(0, record[2])
#         address_editor.insert(0, record[3])
#         age_editor.insert(0, record[4])
#         slcpercent_editor.insert(0, record[5])
#         twelvepercent_editor.insert(0, record[6])
#         phonenumber_editor.insert(0, record[7])
    
#     edit_btn= Button(editor, text=" SAVE ", command=update)
#     edit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# #create text boxes
# username=Entry(root, width=30)
# username.grid(row=0, column=1, padx=20)

# f_name=Entry(root, width=30)
# f_name.grid(row=1, column=1, padx=20)

# l_name= Entry(root, width=30)
# l_name.grid(row=2, column=1)

# address=Entry(root, width=30)
# address.grid(row=3,column=1)

# age=Entry(root,width=30)
# age.grid(row=4,column=1)

# slcpercent=Entry(root, width=30)
# slcpercent.grid(row=5,column=1)

# twelvepercent=Entry(root, width=30)
# twelvepercent.grid(row=6,column=1)

# phonenumber=Entry(root, width=30)
# phonenumber.grid(row=7, column=1)


# #create textbox labels
# username_label=Label(root, text="Username")
# username_label.grid(row=0, column=0)

# f_name_label=Label(root,text="First Name")
# f_name_label.grid(row=1, column=0)

# l_name_label=Label(root,text="Last Name")
# l_name_label.grid(row=2,column=0)

# address_label=Label(root,text="Address")
# address_label.grid(row=3,column=0)

# age_label=Label(root, text="Age")
# age_label.grid(row=4, column=0)

# slcpercent_label=Label(root, text="SLC Percentage")
# slcpercent_label.grid(row=5, column=0)

# twelvepercent_label=Label(root, text="Twelve Percentage")
# twelvepercent_label.grid(row=6,column=0)

# phonenumber_label=Label(root, text="Phone Number")
# phonenumber_label.grid(row=7, column=0)

# #loop through results






# #create submit button
# submit_button= Button(root, text="Add Records", command=submit)
# submit_button.grid(row=9,column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# #create query button
# query_btn= Button(root, text="Show Records",command=query)
# query_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# edit_btn= Button(root, text="Update", command=edit)
# edit_btn.grid(row=14, column=0, columnspan=2, padx=10, pady=10, ipadx=20)

# conn.commit()
# conn.close()
# root.mainloop()


# Facebook:
#     # User table
#     # - Attributes
#     # - Last Name
#     # - Address
#     # - Email
#     # - Password

from tkinter import *