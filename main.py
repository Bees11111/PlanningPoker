import tkinter as tk
from MainMenu import MainMenu

# Crée la fenêtre du menu principal
root = tk.Tk()
root.title("Planning Poker")

#Couleur fond vert
root.configure(bg="#008080")

# Impose une taille minimale de la fenetre
root.minsize(1200,600)

# Cree la frame pour le menu principal
main_menu = MainMenu(root)
main_menu.pack()

# Lance la boucle principale du root
root.mainloop()
