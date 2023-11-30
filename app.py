import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog as fd
from pathlib import Path

class App_GUI():

    def __init__(self):
        
        # Variables 
        self.counter = 0

        # Root
        self.root = ttk.Window(themename="superhero")
        self.root.title("File Transfer")

        self.root.geometry("500x500")

        # Top Label
        self.label_1 = ttk.Label(text="File Transfer Application", font=("Arial", 28), width='wraplenth')
        self.label_1.pack(padx=10, pady=10)

        # Author Label
        self.authorLabel = ttk.Label(text="by kmleevy", font=("Garamond", 16), bootstyle="default")
        self.authorLabel.pack(padx=10, pady=10)


        # Button 1 widget
        self.b1 = ttk.Button(self.root, text="Button 1", bootstyle=(WARNING), command=self.on_click)
        self.b1.pack(padx=10, pady=10)

        # Button 2 widget
        self.b2 = ttk.Button(self.root, text="Open file", bootstyle="success", command=self.select_file)
        self.b2.pack(padx=10, pady=10)
        
        # Dlpay list of files for public view
        self.list = ttk.Treeview(self.root, columns=self.columns, show="headings", bootstyle="primary")
        self.list.pack()

        # List column widget
        self.columns = ("Filename")

        # List header
        self.list.heading("Filename", text="Filename")

        # file list for files
        self.file_list = []


        
        


        self.root.mainloop()

    # Button click function
    def on_click(self):
        self.counter += 1
        if self.counter > 5:
            print("You have clicked this button ", self.counter, " times")
            self.b1.config(text=self.counter, bootstyle="success")
        else:
            print("Hello World!")

    # Button 2 open and write filename to list
    def select_file(self):
        self.filetypes = (
            ('text files', '*.txt'),
            ('All files', '*')
        )

        self.filename = fd.askopenfilename(
            title="Open a file",
            initialdir="/",
            filetypes=self.filetypes
        )
        self.suffix = Path(self.filename).suffix
        self.prefix = Path(self.filename).stem

        self.new_file = self.prefix + self.suffix

        print(self.new_file)

        self.file_list.append(self.new_file)
        print(self.file_list)

        for file in self.file_list:
            self.list.insert('', END, values=file)

        self.file_list.pop()
        
        




App_GUI()