import tkinter as tk
from tkinter import ttk
import argus


class SearchResults(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)
        
        self.results_frame = ttk.Frame(container)
        self.results_frame.columnconfigure(0, weight=1)
        
        self.scrollable_window = self.create_window((0,0), window=self.results_frame, anchor="w")
        
        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))
        
        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())
        
        self.bind("<Configure>", configure_window_size)
        self.results_frame.bind("<Configure>", configure_scroll_region)
        #self.bind_all("<MouseWheel>", self._on_mousewheel)
        
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=2, column=2, sticky="NS")
        
        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0) 
        
    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")    
        
        
    def update_message_widgets(self, show_entry, search_value):
        
        banana = argus.WSearch()
        results = banana.index_search(search_value.get())
        
        for entry in results:
            print(f"Found in the file:{entry}")
            self._create_search_container(entry, show_entry)
        
        if len(results) <= 1:
            result_label = tk.Label(
                self,
                text="No results. Please type something!"
            )
    
            result_label.grid(columnspan=2, row=0, column=0, sticky="EW",)
    
    def _create_search_container(self, entry, show_entry):
        container = ttk.Frame(self.results_frame)
        container.columnconfigure(2, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)
    
        self._create_result_bubble(container, entry, show_entry)
        
    def _create_result_bubble(self, container, entry, show_entry):

        #search button
        self.search_button = ttk.Button(
                    container,
                    text="Inspect the file",
                    command=show_entry,
                    cursor="hand2"
                )
        
        self.search_button.grid(row=0, column=0, sticky="NEW")
        
        result_label = tk.Label(
                container,
                text=entry,
                wraplength=800,
                justify="left",
                anchor="w"
            )
    
        result_label.grid(row=0, column=2)
        
        #separator
        ttk.Separator(container, orient="horizontal").grid(columnspan=3, row=1, column=0, sticky="EW", padx=(5,5), pady=(5,5))         