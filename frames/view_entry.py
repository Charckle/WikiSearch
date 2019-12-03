import tkinter as tk
from tkinter import ttk

class ViewEntry(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller
        
        #grid stuff
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)
     
        #variables
        entry_filename= tk.StringVar()
        entry_filename.set("data//bananaaassa.txt")
        data = tk.StringVar()        
     
        #entry text  
        entry_text = tk.Text(self)
        #populate text
        try:
            with open(f'{entry_filename.get()}', 'r') as file:
                data.set(file.read())
        except:
            data.set("No file selected")
            
        entry_text.grid(row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        entry_text.insert("1.0", data.get())    #the 1 means the line it will insert the text, the 0 is the character. Its weird, but OK
        entry_text["state"] = "disable" 
        #scroll widget
        text_scroll = ttk.Scrollbar(self, orient="vertical", command=entry_text.yview)             #"text.yview" links the scroll widget to the y-axis of the text widget
        text_scroll.grid(row=0, column=1, sticky="ns")
        entry_text["yscrollcommand"] = text_scroll.set               
