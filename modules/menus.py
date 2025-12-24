# project_root/modules/menus.py
import tkinter as tk

class Menubar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        file_items = tk.Menu(tearoff=False)
        file_items.add_command(label='New')
        file_items.add_command(label='Open', command=parent.file_open)
        file_items.add_command(label='Save')
        file_items.add_separator()
        file_items.add_command(label='Exit', command=parent.file_exit)

        edit_items = tk.Menu(tearoff=False)
        run_items = tk.Menu(tearoff=False)

        help_items = tk.Menu(tearoff=False)
        help_items.add_command(label='About', command=parent.about_message)

        self.add_cascade(label='File', menu=file_items)
        self.add_cascade(label='Edit', menu=edit_items)
        self.add_cascade(label='Run', menu=run_items)
        self.add_cascade(label='Help', menu=help_items)