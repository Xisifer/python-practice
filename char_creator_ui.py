from tkinter import * 
from tkinter.ttk import * 
from time import strftime

from char_creator import name_input

# creating tkinter window
root = Tk()
root.title('Menu Demonstration')
  
# Creating Menubar
menubar = Menu(root)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New Character', command = None)


file.add_command(label ='Save', command = None)
# in char_creator.py, store_data saves data to the current Character object.
# TODO: Create a function to save the Character object to memory???

file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
  
# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)
  
# display Menu
root.config(menu = menubar)


# display text
frame = Frame(root)
frame.pack()
button = Button(frame, text = 'Enter Name')
button.pack()

text_input = Entry(root, text="CharName").pack
# text_input.pack(command=name_input)


import tkinter as tk

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()





# mainloop()