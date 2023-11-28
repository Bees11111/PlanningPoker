import tkinter as tk

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class OptionsMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the options menu
        options_label = tk.Label(self, text="Options", font=("Arial", 24, "bold"), bg="#3498db", fg="white")
        options_label.pack(pady=(50, 10))

        # Create buttons for music options and menu with the defined style
        button_music_on = tk.Button(self, text="Music On", command=lambda: print("Music On clicked"), **button_style())
        button_music_on.pack(pady=10)

        button_music_off = tk.Button(self, text="Music Off", command=lambda: print("Music Off clicked"), **button_style())
        button_music_off.pack(pady=10)

        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def show_main_menu(self):
        from main_menu import MainMenu
        # Hide the options menu frame
        self.pack_forget()
        # Show the main menu frame
        MainMenu(self.master).pack()
