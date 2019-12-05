import tkinter as tk
from tkinter import ttk
from frames.results_window import SearchResults

class SearchScreen(ttk.Frame):
    def __init__(self, parent, controller, show_viewentry):
        super().__init__(parent)
        
        self.controller = controller
        
        self.show_entry = show_viewentry
        
        #grid stuff
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)       
        
        #entry search
        self.search_value = tk.StringVar() 
        
        self.search_entry = ttk.Entry(
            self,
            textvariable=self.search_value
        )
        self.search_entry.bind("<KeyRelease>", self.get_results)
        
        self.search_entry.grid(row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        self.search_entry.focus()
        
        #search button
        '''
        self.search_button = ttk.Button(
                    self,
                    text="Run search",
                    command=self.get_results,
                    cursor="hand2"
                )
        
        self.search_button.grid(columnspan=2, row=0, column=1, sticky="NESW", padx=(5,5), pady=(5,5))
        '''
        
        #separator
        ttk.Separator(self, orient="horizontal").grid(columnspan=3, row=1, column=0, sticky="EW", padx=(5,5), pady=(5,5)) 
        
        #canvas
        self.results_frame_main = SearchResults(self, self.controller, self.show_entry)
        self.results_frame_main.grid(columnspan=2, row=2, column=0, sticky="NSEW")
        
    
    def get_results(self, event):
        #print(self.search_value.get()) 
        self.clear()
        self.results_frame_main.update_message_widgets(self.search_value)
        self.after(15, lambda: self.results_frame_main.yview_moveto(0.0))
       
    
    def clear(self):
        list = self.results_frame_main.results_frame.grid_slaves()
        for l in list:
            l.destroy()
            
    