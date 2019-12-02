import tkinter as tk
from tkinter import ttk
from frames import Mainscreen, AddEntry, SearchScreen, SearchResults


class HDSearch(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("HDSearch CRIF")
        self.geometry("1200x600")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)


        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="NESW", padx=(5,5), pady=(5,5))
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        
        self.frames = dict()
        
        mainscreen_frame = Mainscreen(container, self, lambda: self.show_frame(SearchScreen), lambda: self.show_frame(AddEntry))
        addentry_frame = AddEntry(container, self)
        searchscreen_frame = SearchScreen(container, self)
        
        ttk.Separator(container, orient="vertical").grid(row=0, column=1, sticky="ns", padx=(5,5), pady=(5,5))
        
        addentry_frame.grid(row=0, column=0, sticky="NESW")
        mainscreen_frame.grid(row=0, column=2, sticky="NESW")
        searchscreen_frame.grid(row=0, column=0, sticky="NESW")
    
        self.frames[Mainscreen] = mainscreen_frame
        self.frames[AddEntry] = addentry_frame
        self.frames[SearchScreen] = searchscreen_frame
    
        self.show_frame(SearchScreen)        


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = HDSearch()
app.mainloop()