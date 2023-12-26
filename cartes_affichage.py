import tkinter as tk
from cartes_jouer import *

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

class AfficherCartes(tk.Frame):
    valeurs_cartes = {
        "cartes/cartes_0.svg": 0,
        "cartes/cartes_1.svg": 1,
        "cartes/cartes_2.svg": 2,
        "cartes/cartes_3.svg": 3,
        "cartes/cartes_5.svg": 5,
        "cartes/cartes_8.svg": 8,
        "cartes/cartes_13.svg": 13,
        "cartes/cartes_20.svg": 20,
        "cartes/cartes_40.svg": 40,
        "cartes/cartes_100.svg": 100,
        "cartes/cartes_cafe.svg": -1,
        "cartes/cartes_interro.svg": -1
    }

    def __init__(self, master=None, cartes_joueurs=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.cartes_joueurs = cartes_joueurs
        self.create_widgets()
    
    def create_widgets(self):
        cartes = []
        for i, joueur in enumerate(self.cartes_joueurs):
            for j, fichier_svg in enumerate(joueur):
                cartes.append(self.valeurs_cartes[fichier_svg])
                image = self.convertir_svg_en_image(fichier_svg)
                if image:
                    label = tk.Label(self, image=image)
                    label.image = image
                    label.pack(side="left", padx=5)

        #Réinitialiser les cartes des joueurs
        for joueur in self.cartes_joueurs:
             joueur.clear()

        if any(carte != cartes[0] for carte in cartes):
            bouton_refaire_vote = tk.Button(self, text="Refaire le vote")
            bouton_refaire_vote.pack()

    def convertir_svg_en_image(self, fichier_svg):
        dessin = svg2rlg(fichier_svg)
        if dessin is not None:
            image = tk.PhotoImage(data=renderPM.drawToString(dessin, fmt="PNG"))
            return image
        else:
            print(f"Échec de la conversion pour le fichier SVG : {fichier_svg}")
            return None