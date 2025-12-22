import tkinter as tk
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *


root = tk.Tk()

# Global variables
count_result = 0
count_run = True

# Menu functions
def file_exit():
    root.destroy()

def about_message():
    tkinter.messagebox.showinfo('About', '©2025 Bill Hicks')

def digit_counter():
    global count_result
    global count_run

    stop_start_button.pack()

    if count_run:
        count_result += 1
        digit_label.config(text=str(count_result))
        digit_label.after(100,digit_counter)

def color_chooser():
    color = askcolor()
    digit_label.config(bg=color[1])

def button_clicked():
    global count_run
    count_run = not count_run
    # digit_label.config(text=f"Count Run: {count_run}")
    # print('Button clicked')
    if count_run:
        digit_counter()
        stop_start_button.config(text='Stop')
    else:
        stop_start_button.config(text='Start')

root.title('Learning Python')
root.geometry('600x400+200+200')

mainMenu = tk.Menu()
file_items = tk.Menu(tearoff=False)
run_items = tk.Menu(tearoff=False)
help_items = tk.Menu(tearoff=False)

digit_label = tk.Label(root, text='Learning Python',font=200)
# digit_label = tk.Label(root, text=f"Count Run: {count_run}",font=200)
digit_label.pack()
stop_start_button = tk.Button(root, text='Stop', command=button_clicked)
# stop_start_button.pack()

mainMenu.add_cascade(label='File',menu=file_items)
mainMenu.add_cascade(label='Edit')
mainMenu.add_cascade(label='Run',menu=run_items)
mainMenu.add_cascade(label='Help',menu=help_items)

file_items.add_command(label='New')
file_items.add_command(label='Open')
file_items.add_command(label='Save')
file_items.add_command(label='Exit',command=file_exit)

run_items.add_command(label='Digit Counter',command=digit_counter)
run_items.add_command(label='Choose Color',command=color_chooser)

help_items.add_command(label='About',command=about_message)

root.config(menu=mainMenu)
root.mainloop()