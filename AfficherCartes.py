import tkinter as tk
from ChoixCartes import *
from statistics import mean
import datetime

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

# Classe principale pour afficher les cartes
class AfficherCartes(tk.Frame):
    # Dictionnaire associant les chemins des fichiers SVG aux valeurs des cartes
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
        "cartes/cartes_interro.svg": -1
    }

    def __init__(self, master=None, cartes_joueurs=None, backlog=None, mode=0, pseudonyms=[], step=0, isFirstTry=True, savedValues=[], **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.cartes_joueurs = cartes_joueurs
        self.backlog = backlog
        self.mode = mode
        self.pseudonyms = pseudonyms
        self.step = step
        self.isFirstTry = isFirstTry
        self.savedValues = savedValues

        self.create_widgets()
    
    def create_widgets(self):
        values = []

        # Affiche les cartes des joueurs
        for joueur in self.cartes_joueurs:
            for fichier_svg in joueur:
                values.append(self.valeurs_cartes[fichier_svg])
                image = self.convertir_svg_en_image(fichier_svg)
                if image:
                    label = tk.Label(self, image=image)
                    label.image = image
                    label.pack(side="left", padx=5)

        # Effectue l'action en fonction du mode
        self.do_action_by_mode(values)

        # Réinitialise les cartes des joueurs
        for joueur in self.cartes_joueurs:
             joueur.clear()

    def do_action_by_mode(self, values: list):
        # Mode Strict ou première tentative
        if (self.mode == 0 or self.isFirstTry):
            if any(value != values[0] or value == -1 for value in values):
                # Affiche le bouton pour refaire le vote
                bouton_refaire_vote = tk.Button(self, text="Refaire le vote", command=lambda step=self.step: self.show_cards_choice(step), **button_style())
                bouton_refaire_vote.pack(pady=20)
            else:
                # Affiche le message de réussite et le bouton pour la tâche suivante ou retour au menu
                label = tk.Label(self, text="Vous avez réussi à vous mettre d'accord pour la tâche : "+str(self.backlog[self.step]) +" !", font=("TimesNewRoman", 10), bg="#008080", fg="white")
                label.pack()
                self.savedValues.append(values[0])
                if (self.step+1 < len(self.backlog)):
                    nextStepButton = tk.Button(self, text="Tâche suivante", command=lambda step=self.step+1: self.show_cards_choice(step, True), **button_style())
                    nextStepButton.pack(pady=20)
                else:
                    # Ajoute un bouton pour enregistrer les fonctionnalités et valeurs dans un fichier JSON
                    saveFileButton = tk.Button(self, text="Enregistrer dans un JSON", command=self.save_file, **button_style())
                    saveFileButton.pack(pady=20)
                    menuButton = tk.Button(self, text="Retour au menu", command=self.return_to_menu, **button_style())
                    menuButton.pack(pady=20)
        
        # Mode Moyenne
        elif(self.mode == 1):
            if all(value == -1 for value in values):
                # Affiche le message d'erreur et le bouton pour refaire le vote
                label = tk.Label(self, text="Veuillez choisir au moins une carte avec une valeur.", font=("TimesNewRoman", 10), bg="#008080", fg="white")
                label.pack()
                bouton_refaire_vote = tk.Button(self, text="Refaire le vote", command=lambda step=self.step: self.show_cards_choice(step), **button_style())
                bouton_refaire_vote.pack(pady=20)
            else:
                # Calcule la moyenne des valeurs des cartes et affiche le résultat
                goodValues = [value for value in values if (value != -1)]
                meanValues = mean(goodValues)
                allValues = [value for value in self.valeurs_cartes.values() if (value != -1)]
                #print("values :"+str(allValues))
                sorted_list = sorted(allValues, key=lambda x: abs(meanValues- x))
                closest_value = sorted_list[0]
                #print("sorted_list :"+str(sorted_list))
                #print("closest_value :"+str(closest_value))
                label = tk.Label(self, text="La moyenne des valeurs des cartes est de : "+str(meanValues) +"\nAinsi, la carte la plus proche de la moyenne est : "+str(closest_value)+" !", font=("TimesNewRoman", 10), bg="#008080", fg="white")
                label.pack()
                self.savedValues.append(values[0])
                if (self.step+1 < len(self.backlog)):
                    nextStepButton = tk.Button(self, text="Tâche suivante", command=lambda step=self.step+1: self.show_cards_choice(step, True), **button_style())
                    nextStepButton.pack(pady=20)
                else:
                    # Ajoute un bouton pour enregistrer les fonctionnalités et valeurs dans un fichier JSON
                    saveFileButton = tk.Button(self, text="Enregistrer dans un JSON", command=self.save_file, **button_style())
                    saveFileButton.pack(pady=20)
                    menuButton = tk.Button(self, text="Retour au menu", command=self.return_to_menu, **button_style())
                    menuButton.pack(pady=20)
        print("save ="+str(self.savedValues))

    def convertir_svg_en_image(self, fichier_svg):
        dessin = svg2rlg(fichier_svg)
        if dessin is not None:
            image = tk.PhotoImage(data=renderPM.drawToString(dessin, fmt="PNG"))
            return image
        else:
            print(f"Échec de la conversion pour le fichier SVG : {fichier_svg}")
            return None
        
    def show_cards_choice(self, step, isFirstTry=False):
        from ChoixCartes import ChoixCartes
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Retourne au choix des cartes
        ChoixCartes(self.master, self.backlog, self.mode, self.pseudonyms, step=step, isFirstTry=isFirstTry).pack()
    
    def return_to_menu(self):
        from MainMenu import MainMenu
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche le menu
        MainMenu(self.master).pack()

    def save_file(self):
        backlogValues = {}

        for i, task in enumerate(self.backlog):
            backlogTask = {task: self.savedValues[i]}
            backlogValues.update(backlogTask)
        print(str(backlogValues)) 

        nameFile = "backlog"+str(datetime.datetime.now().time()).replace(":", "").replace(".", "")
        print("File :"+nameFile)
        with open(nameFile+".json", 'x') as fichier:
            json.dump(backlogValues, fichier, indent=2)
        messagebox.showinfo("Sauvegarde", "Backlog sauvegardé avec succès.")