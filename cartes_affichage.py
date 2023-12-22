import tkinter as tk
from cartes_jouer import *

class AfficherCartes(tk.Frame):
    def __init__(self, master=None, cartes_joueurs=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.cartes_joueurs = cartes_joueurs
        self.create_widgets()
    
    def create_widgets(self):

        for i, joueur in enumerate(self.cartes_joueurs):
            for j, fichier_svg in enumerate(joueur):
                image = self.convertir_svg_en_image(fichier_svg)
                if image:
                    label = tk.Label(self, image=image)
                    label.image = image
                    label.pack(side="left", padx=5)

        #Réinitialiser les cartes des joueurs
        for joueur in self.cartes_joueurs:
             joueur.clear()

    def convertir_svg_en_image(self, fichier_svg):
        dessin = svg2rlg(fichier_svg)
        if dessin is not None:
            image = tk.PhotoImage(data=renderPM.drawToString(dessin, fmt="PNG"))
            return image
        else:
            print(f"Échec de la conversion pour le fichier SVG : {fichier_svg}")
            return None
