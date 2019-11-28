import tkinter as tk
from tkinter import ttk



class HDSearch(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("HDSearch CRIF")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        
        self.frames = {}
        
        mainscreen_frame = Timer(container, self, lambda: self.show_frame(Settings))
        addentry_frame = Settings(container, self, lambda: self.show_frame(Timer))
        addentry_frame.grid(row=0, column=0, sticky="NESW")
        mainscreen_frame.grid(row=0, column=0, sticky="NESW")
    
        self.frames[MainScreen] = mainscreen_frame
        self.frames[AddEntry] = addentry_frame
    
        self.show_frame(Timer)        


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = HDSearch()
app.mainloop()