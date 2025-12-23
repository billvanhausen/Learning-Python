# import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *


root = Tk()
footer_row = Frame(root, width=600, height=50)
footer_row.grid(row=3, columnspan=3, sticky="s")

# Global variables
count_result = 0
count_run = True
language_list = ['Java', 'PHP', 'Python', 'C#']
language_choice = IntVar()
digit_label = Label(root,font=200)
digit_label.grid(row=0, column=1)
show_languages = BooleanVar()
show_languages.set(True)

def file_open():
    opened_file = askopenfile()
    file_contents = open(opened_file.name)
    tkinter.messagebox.showinfo('File Contents', file_contents.read())

def file_exit():
    root.destroy()

def about_message():
    tkinter.messagebox.showinfo('About', '©2025 Bill Hicks')

def digit_counter():
    global count_result
    global count_run

    stop_start_button.grid(row=2, column=1)

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
    if count_run:
        digit_counter()
        stop_start_button.config(text='Stop')
    else:
        stop_start_button.config(text='Start')

def on_language_change(name, index, mode):
    current_value = language_choice.get()
    current_language = language_list[current_value]
    
    digit_label.config(text=f'Let\'s Learn {current_language}')

language_choice.trace_add('write', on_language_change)
language_choice.set(2)

def toggle_languages():
    global show_languages
    show_languages = not show_languages
    if show_languages:
        footer_row.grid()
    else:
        footer_row.grid_remove()



root.title('Learning Python')
root.geometry('600x400+200+200')
root.grid_columnconfigure(0,weight=1,uniform='root_group')
root.grid_columnconfigure(1,weight=1,uniform='root_group')
root.grid_columnconfigure(2,weight=1,uniform='root_group')
root.grid_rowconfigure(0,weight=1,uniform='root_group')
root.grid_rowconfigure(1,weight=1,uniform='root_group')
root.grid_rowconfigure(2,weight=1,uniform='root_group')
root.grid_rowconfigure(3,weight=1,uniform='root_group')

footer_row.grid_columnconfigure(0,weight=1,uniform='footer_group')
footer_row.grid_columnconfigure(1,weight=1,uniform='footer_group')
footer_row.grid_columnconfigure(2,weight=1,uniform='footer_group')
footer_row.grid_columnconfigure(3,weight=1,uniform='footer_group')

# Menu System
mainMenu = Menu()
file_items = Menu(tearoff=False)
run_items = Menu(tearoff=False)
help_items = Menu(tearoff=False)

mainMenu.add_cascade(label='File',menu=file_items)
mainMenu.add_cascade(label='Edit')
mainMenu.add_cascade(label='Run',menu=run_items)
mainMenu.add_cascade(label='Help',menu=help_items)

file_items.add_command(label='New')
file_items.add_command(label='Open',command=file_open)
file_items.add_command(label='Save')
file_items.add_command(label='Exit',command=file_exit)

run_items.add_command(label='Digit Counter',command=digit_counter)
run_items.add_command(label='Choose Color',command=color_chooser)
run_items.add_checkbutton(label='Show Languages',command=toggle_languages)

help_items.add_command(label='About',command=about_message)

# Content
# digit_label = Label(root, text=f'Let\'s Learn {language_list[language_choice.get()]}',font=200).grid(row=0, column=1)
stop_start_button = Button(root, text='Stop', command=button_clicked)

Radiobutton(footer_row, text=language_list[0], variable=language_choice, value=0).grid(row=0,column=0)
Radiobutton(footer_row, text=language_list[1], variable=language_choice, value=1).grid(row=0,column=1)
Radiobutton(footer_row, text=language_list[2], variable=language_choice, value=2).grid(row=0,column=2)
Radiobutton(footer_row, text=language_list[3], variable=language_choice, value=3).grid(row=0,column=3)

root.config(menu=mainMenu)
toggle_languages()
root.mainloop()