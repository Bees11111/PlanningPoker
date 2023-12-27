import tkinter as tk
import sys

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
# Classe pour la frame du menu principal
class MainMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Cree le label pour la page
        game_name_label = tk.Label(self, text="Planning Poker", font=("Arial", 24, "bold"), bg="#008080", fg="white")
        game_name_label.pack(pady=(50, 10))

        # Cree les boutons
        button_jouer = tk.Button(self, text="Jouer", command=self.show_jouer_menu, **button_style())
        button_tutoriel = tk.Button(self, text="Tutoriel", command=self.show_tutorial_menu, **button_style())
        button_options = tk.Button(self, text="Options", command=self.show_options_menu, **button_style())
        button_quitter = tk.Button(self, text="Quitter", command=self.quitter, **button_style())

        # Packe le tout
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
        from OptionsMenu import OptionsMenu
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche la frame des options
        OptionsMenu(self.master).pack()

    def show_jouer_menu(self):
        from JouerMenu import JouerMenu
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche la frame pour jouer
        JouerMenu(self.master).pack()

    def show_tutorial_menu(self):
        from TutorialMenu import TutorialMenu
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche la frame du tutoriel
        TutorialMenu(self.master).pack()
