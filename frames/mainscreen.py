import tkinter as tk
from tkinter import ttk

class Mainscreen(ttk.Frame):
    def __init__(self, parent, controller, show_searchscreen, show_addscreen):
        super().__init__(parent)
        
        self.controller = controller
        
        #search button
        self.search_button = ttk.Button(
                    self,
                    text="Search",
                    command=show_searchscreen,
                    cursor="hand2"
                )
        
        self.search_button.pack(side="top")
        
        #separator
        ttk.Separator(self, orient="horizontal").pack(side="top", fill ="x", padx=3, pady=3)        
        
        #add entry
        self.add_entry_button = ttk.Button(
                    self,
                    text="Add entry",
                    command=show_addscreen,
                    cursor="hand2"
                )
        
        self.add_entry_button.pack(side="top")           

        #quit button
        self.quit_button = ttk.Button(
                    self,
                    text="Quit",
                    command=controller.destroy,
                    cursor="hand2"
                )
        
        self.quit_button.pack(side="bottom")
        
        #separator
        ttk.Separator(self, orient="horizontal").pack(side="bottom", fill ="x", padx=5, pady=5)
            