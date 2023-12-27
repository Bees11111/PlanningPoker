import tkinter as tk

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

# Classe pour la frame du menu du tutoriel
class TutorialMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Label pour le tutoriel
        tutorial_label = tk.Label(self, text="Tutoriel", font=("Arial", 18, "bold"), bg="#008080", fg="white")
        tutorial_label.pack(pady=(50, 10))

        # Les placeholders pour les tutos
        tutorial_text1 = tk.Label(self, text="Le planning poker est une technique d'estimation Agile dans laquelle les membres de l'équipe attribuent des valeurs relatives aux histoires d'utilisateurs ou aux tâches de manière collaborative.\n\nChaque membre de l'équipe reçoit un ensemble de cartes de planning (0, 1, 2, 3, 5, 8, 13, 20, 40, 100) et une carte Interrogation pour les incertitudes.\n\nChaque membre de l'équipe évalue individuellement la complexité de la tâche en choisissant une carte de planning correspondant à son estimation.\n\nUne fois que chaque membre a choisi sa carte, tous les membres révèlent simultanément leur choix.\n\nSi les estimations varient, le choix se fera en fonction du mode choisi.", bg="#008080", fg="white")
        tutorial_text1.pack(pady=10)

        tutorial_text2 = tk.Label(self, text="Le mode de jeu Strict exige un vote unanime entre les joueurs avant de passer au tour suivant.", bg="#008080", fg="white")
        tutorial_text2.pack(pady=10)

        tutorial_text3 = tk.Label(self, text="Le mode Moyenne calcule la moyenne des votes et attribue à la tâche la valeur la plus proche de la moyenne.\n\nLe processus se répète pour chaque nouvelle tâche à planifier.", bg="#008080", fg="white")
        tutorial_text3.pack(pady=10)

        # Cree un bouton pour revenir au menu principal
        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def show_main_menu(self):
        from MainMenu import MainMenu
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche la frame du menu principal
        MainMenu(self.master).pack()
