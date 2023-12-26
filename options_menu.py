import tkinter as tk

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

class OptionsMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Cree le label pour les options
        options_label = tk.Label(self, text="Options", font=("Arial", 24, "bold"), bg="#008080", fg="white")
        options_label.pack(pady=(50, 10))

        # Cree les boutons
        button_music_on = tk.Button(self, text="Music On", command=lambda: print("Music On clicked"), **button_style())
        button_music_on.pack(pady=10)

        button_music_off = tk.Button(self, text="Music Off", command=lambda: print("Music Off clicked"), **button_style())
        button_music_off.pack(pady=10)

        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def show_main_menu(self):
        from main_menu import MainMenu
        # Vire le contenu de la frame actuelle
        self.pack_forget()
        # Montre la frame du menu principal
        MainMenu(self.master).pack()
