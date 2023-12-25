import tkinter as tk
from main_menu import MainMenu

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class TutorialMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Label pour le tuto
        tutorial_label = tk.Label(self, text="Tutoriel", font=("Arial", 18, "bold"), bg="#3498db", fg="white")
        tutorial_label.pack(pady=(50, 10))

        # Les placeholders pour les tutos
        tutorial_text1 = tk.Label(self, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n", bg="#3498db", fg="white")
        tutorial_text1.pack(pady=10)

        tutorial_text2 = tk.Label(self, text="Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", bg="#3498db", fg="white")
        tutorial_text2.pack(pady=10)

        tutorial_text3 = tk.Label(self, text="Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", bg="#3498db", fg="white")
        tutorial_text3.pack(pady=10)

        # Cree un bouton pour revenir au menu
        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def show_main_menu(self):
        from main_menu import MainMenu
        # Vire le contenu de la frame actuelle
        self.pack_forget()
        # Montre la frame du menu principal
        MainMenu(self.master).pack()
