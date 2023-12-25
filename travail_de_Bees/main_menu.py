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
        # Cree le label pour la page
        game_name_label = tk.Label(self, text="Planning Poker", font=("Arial", 24, "bold"), bg="#3498db", fg="white")
        game_name_label.pack(pady=(50, 10))

        # Cree les boutons
        button_jouer = tk.Button(self, text="Jouer", command=self.show_jouer_menu, **button_style())
        button_tutoriel = tk.Button(self, text="Tutoriel", command=self.show_tutorial_menu, **button_style())
        button_options = tk.Button(self, text="Options", command=self.show_options_menu, **button_style())
        button_quitter = tk.Button(self, text="Quitter", command=self.quitter, **button_style())

        # Pack le tout
        button_jouer.pack(pady=10)
        button_tutoriel.pack(pady=10)
        button_options.pack(pady=10)
        button_quitter.pack(pady=10)

    def quitter(self):
        # Ferme le menu
        self.master.destroy()
        sys.exit()

    def show_options_menu(self):
        # Importé ici pour éviter l'importation circulaire
        from options_menu import OptionsMenu
        # Vire le contenu de la frame actuelle
        self.pack_forget()
        # Montre la frame des options
        OptionsMenu(self.master).pack()

    def show_jouer_menu(self):
        from jouer_menu import JouerMenu
        # Vire le contenu de la frame actuelle
        self.pack_forget()
        # Montre la frame pour jouer
        JouerMenu(self.master).pack()

    def show_tutorial_menu(self):
        from tutorial_menu import TutorialMenu
        # Vire le contenu de la frame actuelle
        self.pack_forget()
        # Montre la frame du tutoriel
        TutorialMenu(self.master).pack()
