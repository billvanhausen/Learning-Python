# project_root/Views/index.py
import tkinter as tk

class Index(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.message_label=tk.Label(self, text='Let\'s Learn Python')
        # self.message_label.grid(row=1, column=0)  
        self.message_label.pack()  

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller