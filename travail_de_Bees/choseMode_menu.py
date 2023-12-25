import tkinter as tk

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class ChoseModeMenu(tk.Frame):
    def __init__(self, master=None, player_count=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.player_count = player_count
        self.create_widgets()

    def create_widgets(self):
        # Importer la classe JouerMenu ici pour éviter l'importation circulaire
        from jouer_menu import JouerMenu

        # Cree le label pour le player count
        count_label_text = f"Vous avez choisi {self.player_count} joueurs.\nChoisissez maintenant un mode de jeu"
        count_label = tk.Label(self, text=count_label_text, font=("Arial", 18, "bold"), bg="#3498db", fg="white")
        count_label.pack(pady=(50, 10))

        # Cree les boutons
        button_strict = tk.Button(self, text="Strict", command=self.choose_strict_mode, **button_style())
        button_strict.pack(pady=10)

        button_moyenne = tk.Button(self, text="Moyenne", command=self.choose_moyenne_mode, **button_style())
        button_moyenne.pack(pady=10)

        button_retour = tk.Button(self, text="Retour", command=self.show_jouer_menu, **button_style())
        button_retour.pack(pady=10)

    def choose_strict_mode(self):
        # Placeholder pour le mode Strict
        print("Mode de jeu Strict choisi")

    def choose_moyenne_mode(self):
        # Placeholder pour le mode Moyenne
        print("Mode de jeu Moyenne choisi")

    def show_jouer_menu(self):
        # Importer la classe JouerMenu ici pour éviter l'importation circulaire
        from jouer_menu import JouerMenu
        # Vire le contenu de la frame actuelle
        self.pack_forget()
        # Montre le précédent menu
        JouerMenu(self.master).pack()

