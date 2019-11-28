import tkinter as tk
from tkinter import ttk

class AddEntry(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller
        
        delete_button = ttk.Button(
                    self,
                    text="exit",
                    command=controller.destroy,
                    cursor="hand2"
                )
        
        delete_button.pack()        