import tkinter as tk

def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class JouerMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create a label for the jouer menu
        jouer_label = tk.Label(self, text="Combien de joueurs veulent jouer ?", font=("Arial", 18, "bold"), bg="#3498db", fg="white")
        jouer_label.pack(pady=(50, 10))

        # Create buttons for player count and menu with the defined style
        for i in range(1, 7):
            button_player_count = tk.Button(self, text=str(i), command=lambda i=i: self.start_game(i), **button_style())
            button_player_count.pack(pady=10)

        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def start_game(self, player_count):
        # Placeholder for starting the game with the selected player count
        print(f"Starting game with {player_count} players")

    def show_main_menu(self):
        from main_menu import MainMenu
        # Hide the jouer menu frame
        self.pack_forget()
        # Show the main menu frame
        MainMenu(self.master).pack()
