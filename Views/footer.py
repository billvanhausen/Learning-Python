# project_root/views/footer.py
import tkinter as tk

class Footer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # create widgets
        self.language_list = ['Java', 'PHP', 'Python', 'C#']
        self.language_choice = tk.IntVar()
        self.language_choice.set(2)
        self.show_languages = tk.BooleanVar()
        self.show_languages.set(True) 

        for index, language in enumerate(self.language_list):
            tk.Radiobutton(self, text=language, variable=self.language_choice, value=index, command=self.on_language_change).grid(row=0,column=index)

        # set the controller
        self.controller = None

    def on_language_change(self):
        
        current_value = self.language_choice.get()
        print(current_value)
        current_language = self.language_list[current_value]
        print(current_language) 
        # message_label.config(text=f'Let us Learn {current_language}')

    def set_controller(self, controller):
        self.controller = controller