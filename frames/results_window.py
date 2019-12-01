import tkinter as tk
from tkinter import ttk

class SearchResults(tk.Canvas):
    def __init(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)
        
        self.results_frame = ttk.Frame(self)
        self.results_frame.columnconfigure(0, weight=1)
        
        self.scrollable_window = self.create_window((0,0), window=self.results_frame, anchor="nw")
        
        def configure_scroll_region(event):
            self.configure(scrollregion=self.canvas.bbox("all"))
        
        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())
        
        self.bind("<Configure>", configure_window_size)
        self.scrollable_frame.bind("<Configure>", configure_scroll_region)
        
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")
        
        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)    