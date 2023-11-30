import tkinter as tk
from tkinter import messagebox

class MyGUI:

    # Intial function
    def __init__(self):

        # Root
        self.root = tk.Tk()
        
        # Label
        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        # Textbox
        self.textbox = tk.Text(self.root, font=('Arial', 18), height=5)
        self.textbox.pack(padx=10, pady=10,)
        self.textbox.bind("<KeyPress>", self.shortcut)

        # State
        self.check_state = tk.IntVar()
        
        # Checkbox
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        # Button
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        

        self.root.mainloop()

    # Show message function
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))