import tkinter as tk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from EntrerBacklog import *
from JouerMenu import pl_count

# Classe pour le choix des cartes
class ChoixCartes(tk.Frame):

    def __init__(self, master=None, backlog=None, mode=None, pseudonyms=[], player_count=pl_count, step=0, isFirstTry=True, savedValues=[], **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.mode = mode
        self.pseudonyms = pseudonyms
        self.backlog = backlog if backlog is not None else []
        self.player_count = player_count
        self.step = step
        self.isFirstTry = isFirstTry
        self.savedValues = savedValues
        # Liste des cartes SVG
        self.fichiers_svg = [
            "cartes/cartes_0.svg", "cartes/cartes_1.svg", "cartes/cartes_2.svg",
            "cartes/cartes_3.svg", "cartes/cartes_5.svg", "cartes/cartes_8.svg",
            "cartes/cartes_13.svg", "cartes/cartes_20.svg", "cartes/cartes_40.svg",
            "cartes/cartes_100.svg", "cartes/cartes_interro.svg"
        ]
        # Dictionnaire pour stocker les images associées aux fichiers SVG
        self.images = {}

        # Liste pour stocker les cartes sélectionnées par chaque joueur
        self.cartes_joueurs = [[] for _ in range(self.player_count)] 

        # Variable pour suivre le tour actuel
        self.tour_actuel = 0

        self.label_tour = tk.Label(self, text=f"Tour du joueur {self.pseudonyms[self.tour_actuel]}\n", font=("TimesNewRoman", 30), bg="#008080", fg="white")
        self.label_tour.pack(side="top", pady=10)

        self.create_widgets()

    def create_widgets(self):
        #print("mode :"+str(self.mode))
        #print("step :"+str(self.step))
        if self.tour_actuel < len(self.backlog):
            self.afficher_texte_backlog()

        # Boucle pour afficher les boutons
        for fichier_svg in self.fichiers_svg:
            image = self.convertir_svg_en_image(fichier_svg)

            if image is not None:
                bouton = tk.Button(self, image=image, command=lambda fichier=fichier_svg: self.afficher_carte(fichier))
                bouton.image = image
                bouton.pack(side="left", padx=5)
    
    def afficher_texte_backlog(self): 
        contenu_backlog = self.backlog[self.step]
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
        # Ajouter la carte à la liste du joueur actuel
        self.cartes_joueurs[self.tour_actuel].append(fichier_svg)

        # Passer au joueur suivant
        self.tour_actuel = (self.tour_actuel + 1) % self.player_count

        self.label_tour.config(text=f"Tour du joueur {self.pseudonyms[self.tour_actuel]}\n")

        # Si tous les joueurs ont joué, afficher les cartes
        if self.tour_actuel == 0:
            self.show_cartes()
    
    def show_cartes(self):
        from AfficherCartes import AfficherCartes
        # Masque la frame actuelle
        self.pack_forget()
        # Affiche la frame pour afficher les cartes
        AfficherCartes(self.master, self.cartes_joueurs, self.backlog, self.mode, self.pseudonyms, self.step, self.isFirstTry, self.savedValues).pack()