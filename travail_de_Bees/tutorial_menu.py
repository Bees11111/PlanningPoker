import tkinter as tk

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class TutorialMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the tutorial menu
        tutorial_label = tk.Label(self, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.", font=("Arial", 14), bg="#3498db", fg="white", wraplength=500)
        tutorial_label.pack(pady=(50, 10))

        # Create a button to return to the main menu
        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def show_main_menu(self):
        from main_menu import MainMenu
        # Hide the tutorial menu frame
        self.pack_forget()
        # Show the main menu frame
        MainMenu(self.master).pack()
