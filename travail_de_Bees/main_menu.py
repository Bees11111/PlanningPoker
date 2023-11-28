import tkinter as tk
import sys

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class MainMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the game name with a larger font
        game_name_label = tk.Label(self, text="Planning Poker", font=("Arial", 24, "bold"), bg="#3498db", fg="white")
        game_name_label.pack(pady=(50, 10))

        # Create buttons with the defined style and padding
        button_jouer = tk.Button(self, text="Jouer", command=self.show_jouer_menu, **button_style())
        button_tutoriel = tk.Button(self, text="Tutoriel", command=self.show_tutorial_menu, **button_style())
        button_options = tk.Button(self, text="Options", command=self.show_options_menu, **button_style())
        button_quitter = tk.Button(self, text="Quitter", command=self.quitter, **button_style())

        # Pack the logo label and buttons to the bottom with padding
        button_jouer.pack(pady=10)
        button_tutoriel.pack(pady=10)
        button_options.pack(pady=10)
        button_quitter.pack(pady=10)

    def quitter(self):
        # Close the main menu window
        self.master.destroy()
        sys.exit()

    def show_options_menu(self):
        # Imported here to avoid CIRCULAR IMPORT
        # This works by not infinitely importing each other at the beginning
        # of the class, and instead, only importing when it's necessary for usage
        from options_menu import OptionsMenu
        # Hide the main menu frame
        self.pack_forget()
        # Show the options menu frame
        OptionsMenu(self.master).pack()

    def show_jouer_menu(self):
        from jouer_menu import JouerMenu
        # Hide the main menu frame
        self.pack_forget()
        # Show the jouer menu frame
        JouerMenu(self.master).pack()

    def show_tutorial_menu(self):
        from tutorial_menu import TutorialMenu
        # Hide the main menu frame
        self.pack_forget()
        # Show the tutorial menu frame
        TutorialMenu(self.master).pack()
