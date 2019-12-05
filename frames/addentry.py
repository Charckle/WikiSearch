import tkinter as tk
from tkinter import ttk, messagebox
import re
import argus



class NewEntry(ttk.Frame):
    def __init__(self, parent, controller, show_ViewEntry):
        super().__init__(parent)

        self.controller = controller

        #grid stuff
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(1, weight=1)

        #variables
        self.entry_filename= tk.StringVar()
        self.data = tk.StringVar()

        #
        #new entry filename
        self.filename_entry_container()
        
        #
        #entry text  
        self.entry_text = tk.Text(self)
        self.entry_text.grid(row=1, column=0, sticky="NESW", padx=(5,5), pady=(5,5))     

        #scroll widget
        text_scroll = ttk.Scrollbar(self, orient="vertical", command=self.entry_text.yview)             #"text.yview" links the scroll widget to the y-axis of the text widget
        text_scroll.grid(row=1, column=1, sticky="ns")
        self.entry_text["yscrollcommand"] = text_scroll.set               

        #button_container
        self.button_container = ttk.Frame(self)
        self.button_container.columnconfigure(0, weight=1)
        self.button_container.grid(columnspan=2, row=2, column=0, sticky="NESW")        

        #Save button
        self.edit_button = ttk.Button(
            self.button_container,
                    text="Save new entry",
                    command=self.save_entry,
                    cursor="hand2"
        )

        self.edit_button.grid(columnspan=1, row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))     

    def filename_entry_container(self):
        self.filename_container = ttk.Frame(self)
        #self.filename_container.columnconfigure(2, weight=1)
        self.filename_container.grid(row=0, column=0, sticky="W", padx=(1, 5), pady=2)        
        
        #filename label
        filename_label = tk.Label(
                self.filename_container,
                text="New entry name: ",
                justify="left",
                anchor="w"
            )
    
        filename_label.grid(row=0, column=0)
        
        #filename input
        self.filename_value = tk.StringVar()
        self.filename_value.set("")
        
        self.filename_entry = ttk.Entry(self.filename_container, textvariable=self.filename_value)
        self.filename_entry.grid(row=0, column=1, sticky="NESW", padx=(5,5), pady=(5,5))
        #self.filename_entry.focus()
        
    def save_entry(self):

        if self.filename_value.get() != "":
            new_filename = "data/" + self.get_valid_filename(self.filename_value.get()) + ".txt"
            print(new_filename)
            with open(f'{new_filename}', 'w') as file:
                file.write(self.entry_text.get("1.0",tk.END))    
    
            #clear inputs
            self.filename_value.set("")
            self.filename_entry.delete(0, 'end')
            self.entry_text.delete('1.0', tk.END)
            
            self.view_mode()
            
            messagebox.showinfo(f"New entry created", f"New entry successfully created under the filename: {new_filename}")
            
        else:
            messagebox.showinfo("New entry name mandatory!", "You must inser the name of the new enrty before saving.")
            self.filename_entry.focus()

    def get_valid_filename(self, s):
    
        """
    
        Return the given string converted to a string that can be used for a clean
    
        filename. Remove leading and trailing spaces; convert other spaces to
    
        underscores; and remove anything that is not an alphanumeric, dash,
    
        underscore, or dot.
    
        >>> get_valid_filename("john's portrait in 2004.jpg")
    
        'johns_portrait_in_2004.jpg'
    
        """
    
        s = str(s).strip().replace(' ', '_')
    
        return re.sub(r'(?u)[^-\w.]', '', s)    