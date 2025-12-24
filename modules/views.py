import tkinter as tk

class My_frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.msg_label = tk.Label(self, text='Hello World!', font=('Trebuchet MS', 30))
        self.msg_label.grid(row=0, columnspan=3, pady=10)

        # Create a few buttons
        self.my_button1 = tk.Button(self, text='change', command=self.change)
        self.my_button2 = tk.Button(self, text='change', command=self.change)
        self.my_button3 = tk.Button(self, text='change', command=self.change)

        self.my_button1.grid(row=1, column=0, padx=10)
        self.my_button2.grid(row=1, column=1, padx=10)
        self.my_button3.grid(row=1, column=2, padx=10)

        self.status = True

    def change(self):
        self.status = not self.status
        if self.status:
            self.msg_label.config(text='Hello World!')
        else:
            self.msg_label.config(text='Goodbye World!')
