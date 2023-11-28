from tkinter import *
import tkinter as tk

#Création de la fenêtre principale de l'application
fenetre_principale = tk.Tk()

#Fonction pour afficher la page principale
def afficher_page_principale():

    #Titre de l'application
    texte1 = tk.Label(fenetre_principale, text="\n\nPlanning Poker\n\n", font=("TimesNewRoman", 30), bg="#008080", fg="white")
    texte1.pack()

    #Création d'un cadre pour contenir le bouton "Jouer" avec une bordure blanche (esthétique)
    contour_bouton = tk.Frame(fenetre_principale, highlightbackground = "white", highlightthickness = 2, bd=0)
    contour_bouton.pack()

    #Création d'un bouton "Jouer" pour ouvrir une nouvelle fenêtre
    bouton_jouer = tk.Button(contour_bouton, text="Jouer", command=ouvrir_nouvelle_fenetre, font=("TimesNewRoman", 20), bg="#008080", fg="white")
    bouton_jouer.pack()

#Fonction pour ouvrir une nouvelle fenêtre
def ouvrir_nouvelle_fenetre():
    fenetre_principale.withdraw()  #Masquer la première fenêtre
    nouvelle_fenetre = tk.Toplevel(fenetre_principale) #Création nouvelle fenetre en tant que sous-fenetre de la fenetre principale
    config_fenetre(nouvelle_fenetre)

    #Titre
    label = tk.Label(nouvelle_fenetre, text="\n\nMenu\n\n", font=("TimesNewRoman", 30), bg="#008080", fg="white")
    label.pack()

    #Création d'un cadre pour contenir le bouton "Fermer" avec une bordure blanche (esthétique)
    contour_bouton = tk.Frame(nouvelle_fenetre, highlightbackground = "white", highlightthickness = 2, bd=0)
    contour_bouton.pack()

    #Création d'un bouton "Fermer" pour fermer la nouvelle fenêtre
    bouton_fermer = tk.Button(contour_bouton, text="Fermer", command=lambda: fermer_fenetre(nouvelle_fenetre), font=("TimesNewRoman", 20), bg="#008080", fg="white")
    bouton_fermer.pack()

#Fonction pour fermer une fenêtre
def fermer_fenetre(fenetre):
    fenetre.destroy()

#Fonction pour configurer les paramètres d'une fenêtre
def config_fenetre(fenetre) :
    fenetre.title("Application Planning Poker") #nom de la fenetre
    fenetre.config(bg="#008080") #couleur du fond
    fenetre.geometry("640x480") #taille de la fenetre