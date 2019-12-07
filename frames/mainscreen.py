import tkinter as tk
from tkinter import ttk
import argus

class Mainscreen(ttk.Frame):
    def __init__(self, parent, controller, show_searchscreen):
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
        ttk.Separator(self, orient="horizontal").pack(side="bottom", fill ="x", padx=5, pady=5)
        

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
        
        #index button
        self.index_create_button = ttk.Button(
                    self,
                    text="Create index",
                    command=self.index_create,
                    cursor="hand2"
                )
        
        self.index_create_button.pack(side="bottom")
        
           
    
    def index_create(self):
        
        print("Making the freaking index. This is gonna take some time, brace yourself!") 
        new_index = argus.WSearch()
        new_index.index_create_from_wiki("https://wiki.razor.si")
        print("Index created.") 