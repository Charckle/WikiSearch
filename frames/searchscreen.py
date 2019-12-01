import tkinter as tk
from tkinter import ttk

class SearchScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller
        
        #grid stuff
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)       
        
        #entry search
        self.search_value = tk.StringVar()
        
        self.search_entry = ttk.Entry(self, textvariable=self.search_value)
        self.search_entry.grid(row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        self.search_entry.focus()        
        
        #search button
        self.search_button = ttk.Button(
                    self,
                    text="Run search",
                    command=self.search_entered,
                    cursor="hand2"
                )
        
        self.search_button.grid(columnspan=2, row=0, column=1, sticky="NESW", padx=(5,5), pady=(5,5))
        
        #separator
        ttk.Separator(self, orient="horizontal").grid(columnspan=3, row=1, column=0, sticky="EW", padx=(5,5), pady=(5,5)) 
        
        #canvas
        self.canvas = tk.Canvas(self)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_window = self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        
        def configure_scroll_region(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            
        self.scrollable_frame.bind("<Configure>", configure_scroll_region)
        
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.grid(row=2, column=2, sticky="NS")
        self.canvas.grid(columnspan=2, row=2, column=0, sticky="NSEW")
        #bind enter
        #controller.bind("<Return>", self.exit)
        #controller.bind("<KP_Enter>", self.exit)
    
    def search_entered(self):
        print(self.search_value.get())   