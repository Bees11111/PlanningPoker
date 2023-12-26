import tkinter as tk
from main_menu import MainMenu

# Cree la fenetre du menu principal
root = tk.Tk()
root.title("Planning Poker")

# Met le fond en bleu
root.configure(bg="#3498db")

# Impose une taille minimale de la fenetre
root.minsize(800, 500)

# Cree la frame pour le main menu
main_menu = MainMenu(root)

# Pack le menu
main_menu.pack()

# Lance le root
root.mainloop()
