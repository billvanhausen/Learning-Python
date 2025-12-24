# project_root/app.py
import tkinter as tk
from modules.views import My_frame
from modules.menus import Menubar

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Title, icon, size
        self.title('Tkinter - Object Oriented Programming')
        self.iconbitmap('./images/digitalhicks.ico')
        self.geometry('600x400')

        self.menu = Menubar(self)
        self.config(menu=self.menu)

        # Create a frame outside of the __init__ function
        My_frame(self).pack(pady=20)

    def file_exit(self):
        self.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()