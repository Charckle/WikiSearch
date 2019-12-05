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
        self.entry_filename= tk.StringVar()
        self.entry_filename.set("")
        #self.entry_filename.set(self.controller.selected_entry_filename)
        self.data = tk.StringVar()
        
        #entry text  
        self.entry_text = tk.Text(self)
        self.entry_text.grid(row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        #get data from file and populate
        self.populate_from_file()        
        
        #scroll widget
        text_scroll = ttk.Scrollbar(self, orient="vertical", command=self.entry_text.yview)             #"text.yview" links the scroll widget to the y-axis of the text widget
        text_scroll.grid(row=0, column=1, sticky="ns")
        self.entry_text["yscrollcommand"] = text_scroll.set               
        
        #button_container
        self.button_container = ttk.Frame(self)
        self.button_container.columnconfigure(0, weight=1)
        self.button_container.grid(columnspan=2, row=1, column=0, sticky="NESW")        
        
        #Edit button populate
        self.view_mode()
    

    def populate_from_file(self):
        #make the text widget editable
        self.entry_text["state"] = "normal"          
        #delete text widget content
        self.entry_text.delete('1.0', tk.END)
        print(self.entry_filename.get())
        try:
            with open(f'{self.entry_filename.get()}', 'r') as file:
                self.data.set(file.read())
                print(self.entry_filename.get())
        except:
            self.data.set("No file selected")
        
        self.entry_text.insert("1.0", self.data.get())    #the 1 means the line it will insert the text, the 0 is the character. Its weird, but OK
        self.entry_text["state"] = "disable"         
    
    def save_entry(self):
        self.clear()
        
        with open(f'{self.entry_filename.get()}', 'w') as file:
            file.write(self.entry_text.get("1.0",tk.END))    
    
        
        self.view_mode()
        
        
    def edit_mode(self):
        self.clear()
        self.entry_text["state"] = "normal"   
        
        #Save button
        self.edit_button = ttk.Button(
                    self.button_container,
                    text="Save entry",
                    command=self.save_entry,
                    cursor="hand2"
                )
        
        self.edit_button.grid(columnspan=1, row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        
        #separator
        ttk.Separator(self.button_container, orient="horizontal").grid(columnspan=2, row=1, column=0, sticky="EW", padx=(5,5), pady=(5,5))         
        
        #Cancel button
        self.edit_button = ttk.Button(
                    self.button_container,
                    text="Cancel editing entry",
                    command=self.view_mode,
                    cursor="hand2"
                )
        
        self.edit_button.grid(columnspan=1, row=2, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
    
    def view_mode(self):
        self.clear()
        
        self.populate_from_file()
        
        #Edit button
        self.edit_button = ttk.Button(
                    self.button_container,
                    text="Edit entry",
                    command=self.edit_mode,
                    cursor="hand2"
                )
        
        self.edit_button.grid(columnspan=1, row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))     
    
    def clear(self):
        list = self.button_container.grid_slaves()
        for l in list:
            l.destroy()    