import tkinter as tk
from choseMode_menu import ChoseModeMenu 

pseudo = None

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#388E8E", "fg": "white", "height": 2, "width": 15}

class ChosePseudoMenu(tk.Frame):
    def __init__(self, master=None, player_count=None, **kwargs):
        super().__init__(master, bg="#008080", **kwargs)
        self.master = master
        self.player_count = player_count
        self.pseudonyms = []  # Initialize the pseudonyms list
        self.current_player = 1
        self.create_widgets()

    def create_widgets(self):
        count_label_text = f"Vous avez choisi {self.player_count} joueurs.\nChoisissez un pseudonyme pour le joueur {self.current_player}"
        self.count_label = tk.Label(self, text=count_label_text, font=("Arial", 18, "bold"), bg="#008080", fg="white")
        self.count_label.pack(pady=(50, 10))

        pseudonym_entry = tk.Entry(self, font=("Arial", 10), width=20)
        pseudonym_entry.pack(pady=10)

        pseudonym_entry.bind("<Return>", lambda event: self.submit_pseudonym(pseudonym_entry))

        submit_button = tk.Button(self, text="Suivant", command=lambda: self.submit_pseudonym(pseudonym_entry), **button_style())
        submit_button.pack(pady=10)

    def submit_pseudonym(self, entry_widget):
        pseudonym = entry_widget.get()

        if pseudonym:
            self.pseudonyms.append(pseudonym)
            entry_widget.delete(0, tk.END)

            if len(self.pseudonyms) < self.player_count:
                self.update_label()
            else:
                self.show_jouer_menu(self.pseudonyms)

    def update_label(self):
        self.current_player += 1
        count_label_text = f"Vous avez choisi {self.player_count} joueurs.\nChoisissez un pseudonyme pour le joueur {self.current_player}"
        self.count_label.config(text=count_label_text)

    def show_jouer_menu(self, pseudonyms):
        global pseudo
        pseudo = pseudonyms
         # Import JouerMenu here
        self.pack_forget()
        ChoseModeMenu(self.master, pseudonyms=pseudonyms).pack()