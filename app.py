import tkinter as tk
from tkinter import ttk
from frames import Mainscreen, SearchScreen, SearchResults


class HDSearch(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Wiki Search")
        self.geometry("600x300")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)


        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        
        self.frames = dict()
        
        self.mainscreen_frame = Mainscreen(container, self, lambda: self.show_frame(SearchScreen))
        self.searchscreen_frame = SearchScreen(container, self)
        
        ttk.Separator(container, orient="vertical").grid(row=0, column=1, sticky="ns", padx=(5,5), pady=(5,5))
        
        self.mainscreen_frame.grid(row=0, column=2, sticky="NESW")
        self.searchscreen_frame.grid(row=0, column=0, sticky="NESW")
    
        self.frames[Mainscreen] = self.mainscreen_frame
        self.frames[SearchScreen] = self.searchscreen_frame
    
        self.show_frame(SearchScreen)        


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = HDSearch()
app.mainloop()