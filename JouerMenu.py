import tkinter as tk
from ChosePseudoMenu import ChosePseudoMenu

# Variable globale pour stocker le nombre de joueurs
pl_count = None

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

# Classe pour la fenêtre du menu de jeu
class JouerMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Cree le label pour la page
        jouer_label = tk.Label(self, text="Combien de joueurs veulent jouer ?", font=("Arial", 18, "bold"), bg="#008080", fg="white")
        jouer_label.pack(pady=(50, 10))

        # Cree un bouton pour chaque possibilité de nombre de joueurs
        for i in range(2, 5):
            button_player_count = tk.Button(self, text=str(i), command=lambda i=i: self.choose_player_count(i), **button_style())
            button_player_count.pack(pady=10)

        # Bouton pour revenir au menu principal
        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def choose_player_count(self, player_count):
        global pl_count
        pl_count = player_count
        # Masque la frame actuelle
        self.pack_forget()
        #Affiche la frame du choix des pseudonymes avec le nombre de joueurs choisi
        ChosePseudoMenu(self.master, player_count=player_count).pack()
        
    def show_main_menu(self):
        from MainMenu import MainMenu
        # Masque la frame actuelle
        self.pack_forget()
        # Retourne au menu principal
        MainMenu(self.master).pack()