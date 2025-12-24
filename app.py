# project_root/app.py
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from modules.views import My_frame
from modules.menus import Menubar

class App(tk.Tk):
    # App Initializations
    def __init__(self):
        super().__init__()

        self.title('Tkinter - Object Oriented Programming')
        self.iconbitmap('./images/digitalhicks.ico')
        self.geometry('600x400')

        self.menu = Menubar(self)
        self.config(menu=self.menu)

        # Create a frame outside of the __init__ function
        My_frame(self).pack(pady=20)

    # App functions
    def file_exit(self):
        self.destroy()

    def about_message(self):
        messagebox.showinfo('About Parent', '©2025 Bill Hicks')

    def file_open(self):
        file = filedialog.askopenfile('r')
        contents = open(file.name)
        messagebox.showinfo('File Contents', contents.read())

# Start App Main Loop
if __name__ == '__main__':
    app = App()
    app.mainloop()