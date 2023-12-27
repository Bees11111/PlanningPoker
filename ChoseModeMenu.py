import tkinter as tk

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

# Classe pour le menu de choix de mode de jeu
class ChoseModeMenu(tk.Frame):
    def __init__(self, master=None, pseudonyms=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.pseudonyms = pseudonyms
        self.create_widgets()

    def create_widgets(self):
        newline_label = tk.Label(self, text="\n", font=("Arial", 14, "bold"), bg="#008080", fg="white")
        newline_label.pack()

        # Crée le label pour le nombre de joueurs
        for i, pseudo in enumerate(self.pseudonyms, start=1):
            label_text = f"Le pseudo du joueur {i} : {pseudo}"
            count_label = tk.Label(self, text=label_text, font=("Arial", 10, "bold"), bg="#008080", fg="white")
            count_label.pack(pady=0, padx=10)  

        choice_message = "\nChoisissez maintenant un mode de jeu"
        choice_label = tk.Label(self, text=choice_message, font=("Arial", 18, "bold"), bg="#008080", fg="white")
        choice_label.pack(pady=10)

        # Crée les boutons
        button_strict = tk.Button(self, text="Strict", command=self.choose_strict_mode, **button_style())
        button_strict.pack(pady=10)

        button_moyenne = tk.Button(self, text="Moyenne", command=self.choose_moyenne_mode, **button_style())
        button_moyenne.pack(pady=10)

        button_retour = tk.Button(self, text="Retour", command=self.show_retour_menu, **button_style())
        button_retour.pack(pady=10)

    def choose_strict_mode(self):
        from EntrerBacklog import EntrerBacklog
        # Placeholder pour le mode Strict
        #print("Mode de jeu Strict choisi")
        self.pack_forget()
        EntrerBacklog(self.master, mode=0, pseudonyms=self.pseudonyms).pack()

    def choose_moyenne_mode(self):
        from EntrerBacklog import EntrerBacklog
        # Placeholder pour le mode Moyenne
        #print("Mode de jeu Moyenne choisi")
        self.pack_forget()
        EntrerBacklog(self.master, mode=1, pseudonyms=self.pseudonyms).pack()
    
    def show_retour_menu(self):
        from JouerMenu import JouerMenu
        self.pack_forget()
        JouerMenu(self.master).pack()

    def show_jouer_menu(self):
        from EntrerBacklog import EntrerBacklog
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche le menu précédent
        EntrerBacklog(self.master).pack()
