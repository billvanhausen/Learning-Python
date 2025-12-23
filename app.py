# project_root/app.py
import tkinter as tk
from Views.index import Index
from Views.footer import Footer
import Modules.main_menu

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Hello MVC')
        self.geometry('600x400+200+200')

        # Create a model
        # Create a view and place it on the root window
        view = Index(self)
        view.pack(anchor='n')

        language = Footer(self)
        language.pack(anchor='s')
        # Create a controller
        # Set the controller to view

        # Menu system
        menubar = tk.Menu(self)
        file_menu = tk.Menu(tearoff=0)
        help_menu = tk.Menu(tearoff=0)

        file_menu.add_command(label='New')
        file_menu.add_command(label='Open')
        file_menu.add_command(label='Save')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)

        help_menu.add_command(label='About', command=Modules.main_menu.about_message)


        menubar.add_cascade(label='File', menu=file_menu)
        menubar.add_cascade(label='Edit')
        menubar.add_cascade(label='Help', menu=help_menu)
        
        self.config(menu=menubar)

if __name__ == '__main__':
    app = App()
    # app.config(menu=mainMenu)
    app.mainloop()