import json
import tkinter as tk
from tkinter import messagebox, filedialog

# Fonction pour définir le style des boutons
def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 1, "width": 20}

# Classe pour la fenêtre d'entrée du backlog
class EntrerBacklog(tk.Frame):
    def __init__(self, master=None, mode=0, pseudonyms=[], **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.mode = mode
        self.pseudonyms = pseudonyms
        self.backlog = []
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=40)
        self.charger_backlog()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Backlog :", font=("TimesNewRoman", 20), bg="#008080", fg="white")
        self.label.pack(pady=10)

        # Listbox pour afficher les fonctionnalités du backlog
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=50)
        for fonctionnalite in self.backlog:
            self.listbox.insert(tk.END, fonctionnalite)
        self.listbox.pack(pady=10)

        # Cadre et bouton pour ajouter une nouvelle fonctionnalité
        entry_frame = tk.Frame(self, bg="#008080")
        entry_frame.pack(side=tk.TOP, pady=10)

        # Champ de saisie pour ajouter de nouvelles fonctionnalités
        self.entry = tk.Entry(entry_frame, width=40)
        self.entry.pack(side=tk.LEFT)

        # Bouton pour ajouter une fonctionnalité
        self.ajouter_button = tk.Button(entry_frame, text="Ajouter", command=self.ajouter_fonctionnalite, bg="#388E8E", fg="white", relief= tk.GROOVE)
        self.ajouter_button.pack(side=tk.LEFT, padx=5)
        
        # Nouvelle ligne pour les boutons suivants
        self.button_row_frame = tk.Frame(self, bg="#008080")
        self.button_row_frame.pack(side=tk.TOP)      

        # Bouton pour charger le backlog depuis un fichier
        self.charger_fichier_button = tk.Button(self.button_row_frame, text="Charger depuis un fichier", command=self.load_backlog_from_file, **button_style())
        self.charger_fichier_button.pack(side=tk.LEFT, pady=5)
        
        # Bouton pour sauvegarder le backlog
        self.sauvegarder_button = tk.Button(self.button_row_frame, text="Sauvegarder", command=self.sauvegarder_backlog, **button_style())
        self.sauvegarder_button.pack(side=tk.LEFT, padx=5)

        # Bouton pour effacer la liste
        self.effacer_liste_button = tk.Button(self.button_row_frame, text="Effacer la liste", command=self.effacer_liste, **button_style())
        self.effacer_liste_button.pack(side=tk.LEFT, pady=10)

        # Liaison de la touche "Entrée" pour ajouter une fonctionnalité
        self.entry.bind("<Return>", lambda event: self.ajouter_fonctionnalite())

        # Bouton pour passer à la fenêtre ChoixCartes
        self.commencer = tk.Button(self, text="  Commencer  ", command=self.show_cartes_jouer, **button_style())
        self.commencer.pack(pady=10)

    def load_backlog_from_file(self):
         #Fonction pour charger le backlog depuis un fichier JSON
         fichier_json = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
         if fichier_json:
             self.charger_backlog(fichier_json)

    def charger_backlog(self, fichier_json=None):
        # Fonction pour charger le backlog depuis un fichier JSON
        try:
            with open(fichier_json or "backlog.json", 'r') as fichier:
                self.backlog = json.load(fichier)
        except FileNotFoundError:
            print("Le fichier n'existe pas.")

        self.listbox.delete(0, tk.END)  # Efface la liste actuelle
        for fonctionnalite in self.backlog:
            self.listbox.insert(tk.END, fonctionnalite)

    def ajouter_fonctionnalite(self):
        # Fonction pour ajouter une nouvelle fonctionnalité au backlog
        nouvelle_fonctionnalite = self.entry.get()
        if nouvelle_fonctionnalite:
            self.backlog.append(nouvelle_fonctionnalite)
            self.listbox.insert(tk.END, nouvelle_fonctionnalite)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Erreur", "Veuillez entrer une fonctionnalité.")

    def sauvegarder_backlog(self):
        # Fonction pour sauvegarder le backlog dans un fichier JSON
        with open("backlog.json", 'w') as fichier:
            json.dump(self.backlog, fichier, indent=2)
        messagebox.showinfo("Sauvegarde", "Backlog sauvegardé avec succès.")
    
    def effacer_liste(self):
        self.listbox.delete(0, tk.END)
        self.backlog = []

    def show_cartes_jouer(self):
        # print ("mode :"+str(self.mode))
        # print ("pseudo :"+str(self.pseudonyms))
        from ChoixCartes import ChoixCartes
        # Masque le contenu de la frame actuelle
        self.pack_forget()
        # Affiche la frame pour le choix des cartes
        ChoixCartes(self.master, self.backlog, self.mode, self.pseudonyms).pack()