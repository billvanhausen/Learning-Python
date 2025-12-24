# project_root/modules/menus.py
import tkinter as tk
from tkinter import messagebox

def file_open():
    pass

# def file_exit(parent):
#     print('File Exit')
#     print(str(parent))
#     # parent.destroy()

def about_message():
    messagebox.showinfo('About', '©2025 Bill Hicks')

class Menubar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        file_items = tk.Menu(tearoff=False)
        file_items.add_command(label='New')
        file_items.add_command(label='Open', command=file_open)
        file_items.add_command(label='Save')
        file_items.add_separator()
        file_items.add_command(label='Exit', command=parent.file_exit)

        edit_items = tk.Menu(tearoff=False)
        run_items = tk.Menu(tearoff=False)

        help_items = tk.Menu(tearoff=False)
        help_items.add_command(label='About', command=about_message)

        self.add_cascade(label='File', menu=file_items)
        self.add_cascade(label='Edit', menu=edit_items)
        self.add_cascade(label='Run', menu=run_items)
        self.add_cascade(label='Help', menu=help_items)