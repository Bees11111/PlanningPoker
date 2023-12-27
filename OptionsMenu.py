import tkinter as tk
import pygame

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

# Classe pour la frame du menu des options
class OptionsMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.create_widgets()

        # Initialise Pygame
        pygame.init()

        # Chemin du fichier audio
        self.music_file = "musique.mp3"

        # Initialise le lecteur audio Pygame
        pygame.mixer.init()

    def create_widgets(self):
        # Cree le label pour les options
        options_label = tk.Label(self, text="Options", font=("Arial", 24, "bold"), bg="#008080", fg="white")
        options_label.pack(pady=(50, 10))

        # Cree les boutons
        button_music_on = tk.Button(self, text="Music On", command=self.play_music, **button_style())
        button_music_on.pack(pady=10)

        button_music_off = tk.Button(self, text="Music Off", command=self.stop_music, **button_style())
        button_music_off.pack(pady=10)

        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)
    
    def play_music(self):
        # Charge et joue la musique
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)  # -1 signifie jouer en boucle

    def stop_music(self):
        # Arrête la musique
        pygame.mixer.music.stop()

    def show_main_menu(self):
        from MainMenu import MainMenu
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche la frame du menu principal
        MainMenu(self.master).pack()
