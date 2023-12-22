import os
import sys
import tkinter as tk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from backlog import *

class ChoixCartes(tk.Frame):
    def __init__(self, master=None, backlog=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.backlog = backlog if backlog is not None else []
        self.create_widgets()

    def create_widgets(self):
        #Liste des cartes SVG
        self.fichiers_svg = [
            "cartes/cartes_0.svg", "cartes/cartes_1.svg", "cartes/cartes_2.svg",
            "cartes/cartes_3.svg", "cartes/cartes_5.svg", "cartes/cartes_8.svg",
            "cartes/cartes_13.svg", "cartes/cartes_20.svg", "cartes/cartes_40.svg",
            "cartes/cartes_100.svg", "cartes/cartes_cafe.svg", "cartes/cartes_interro.svg"
        ]

        #Dictionnaire pour stocker les images associées aux fichiers SVG
        self.images = {}

        #Liste pour stocker les cartes sélectionnées par chaque joueur
        self.cartes_joueurs = [[] for _ in range(3)]  #Trois joueurs pour l'instant

        #Variable pour suivre le tour actuel
        self.tour_actuel = 0

        self.label_tour = tk.Label(self, text="Tour du joueur 1\n", font=("TimesNewRoman", 30), bg="#008080", fg="white")
        self.label_tour.pack(side="top", pady=10)

        if self.tour_actuel < len(self.backlog):
            self.afficher_texte_backlog()

        #Masque les avertissements relatifs à la recherche de polices
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

        #Boucle pour afficher les boutons
        for fichier_svg in self.fichiers_svg:
            image = self.convertir_svg_en_image(fichier_svg)
            if image:
                bouton = tk.Button(self, image=image, command=lambda svg=fichier_svg: self.afficher_carte(svg))
                bouton.image = image
                bouton.pack(side="left", padx=5)
    
    def afficher_texte_backlog(self): 
        contenu_backlog = self.backlog[self.tour_actuel]
        texte = f"Définissez la difficulté de : {contenu_backlog} \n"

        label_texte_backlog = tk.Label(self, text=texte, font=("TimesNewRoman", 16), bg="#008080", fg="white")
        label_texte_backlog.pack(side="top", pady=10)
    
    def convertir_svg_en_image(self, fichier_svg):
        dessin = svg2rlg(fichier_svg)
        if dessin is not None:
            image = tk.PhotoImage(data=renderPM.drawToString(dessin, fmt="PNG"))
            return image
        else:
            print(f"Échec de la conversion pour le fichier SVG : {fichier_svg}")
            return None
        
    def afficher_carte(self, fichier_svg):
        
        #print(f"Clic sur la carte : {fichier_svg} (Joueur {self.tour_actuel + 1})")

        #Ajouter la carte à la liste du joueur actuel
        self.cartes_joueurs[self.tour_actuel].append(fichier_svg)

        #Passer au joueur suivant
        self.tour_actuel = (self.tour_actuel + 1) % 3

        self.label_tour.config(text=f"Tour du joueur {self.tour_actuel + 1}\n")

        #Si trois joueurs ont joué, afficher les cartes au centre
        if self.tour_actuel == 0:
            self.show_cartes()
    
    def show_cartes(self):
        from cartes_affichage import AfficherCartes
        #Hide the main menu frame
        self.pack_forget()
        #Show the options menu frame
        AfficherCartes(self.master, self.cartes_joueurs).pack()