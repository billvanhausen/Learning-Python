# project_root/Views/index.py
import tkinter as tk
import Views.footer as footer

class Index(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.message_label=tk.Label(self, text='Let\'s Learn Python')
        self.message_label.pack(anchor='n')  
        # set the controller
        self.controller = None

    def set_message(self, msg):  
        self.message_label.config(text=msg)

    def set_controller(self, controller):
        self.controller = controller