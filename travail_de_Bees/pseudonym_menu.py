import tkinter as tk


#
#  PAS ENCORE FONCTIONNEL, A IGNORER
#


def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class PseudonymMenu(tk.Frame):
    def __init__(self, master=None, player_count=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.player_count = player_count
        self.pseudonyms = []
        self.current_player = 1  # To keep track of the current player selecting a pseudonym
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the chosen player count
        count_label_text = f"Vous avez choisi {self.player_count} joueurs.\nChoisissez un pseudonyme pour le joueur {self.current_player}"
        count_label = tk.Label(self, text=count_label_text, font=("Arial", 18, "bold"), bg="#3498db", fg="white")
        count_label.pack(pady=(50, 10))

        # Create an entry for the player to input their pseudonym
        pseudonym_entry = tk.Entry(self, font=("Arial", 14), width=20)
        pseudonym_entry.pack(pady=10)

        # Create a button to submit the pseudonym and proceed to the next player or game mode
        submit_button = tk.Button(self, text="Suivant", command=lambda: self.submit_pseudonym(pseudonym_entry), **button_style())
        submit_button.pack(pady=10)

    def submit_pseudonym(self, entry_widget):
        # Get the entered pseudonym
        pseudonym = entry_widget.get()

        # Save the pseudonym for the current player
        self.pseudonyms.append(pseudonym)

        # Clear the entry widget
        entry_widget.delete(0, tk.END)

        # Check if all players have chosen a pseudonym
        if self.current_player < self.player_count:
            # Update the label for the next player
            self.current_player += 1
            count_label_text = f"Vous avez choisi {self.player_count} joueurs.\nChoisissez un pseudonyme pour le joueur {self.current_player}"
            entry_widget.set(count_label_text)
        else:
            # All players have chosen a pseudonym, proceed to the next step (game mode)
            self.show_chose_mode_menu()

    def show_chose_mode_menu(self):
        # Import the ChoseModeMenu class here to avoid circular import
        from choseMode_menu import ChoseModeMenu
        # Destroy the pseudonym menu frame
        self.destroy()
        # Show the chose mode menu frame with the previously chosen player count and pseudonyms
        ChoseModeMenu(self.master, player_count=self.player_count, pseudonyms=self.pseudonyms).pack()
