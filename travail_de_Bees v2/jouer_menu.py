import tkinter as tk


def button_style():
    return {"bd": 2, "relief": tk.GROOVE, "bg": "#5DADE2", "fg": "white", "height": 2, "width": 15}

class JouerMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#3498db", **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        jouer_label = tk.Label(self, text="Combien de joueurs veulent jouer ?", font=("Arial", 18, "bold"), bg="#3498db", fg="white")
        jouer_label.pack(pady=(50, 10))

        for i in range(2, 5):
            button_player_count = tk.Button(self, text=str(i), command=lambda i=i: self.choose_player_count(i), **button_style())
            button_player_count.pack(pady=10)

        button_menu = tk.Button(self, text="Menu", command=self.show_main_menu, **button_style())
        button_menu.pack(pady=10)

    def choose_player_count(self, player_count):
        from choseMode_menu import ChoseModeMenu
        self.pack_forget()
        ChoseModeMenu(self.master, player_count=player_count).pack()

    def show_main_menu(self):
        from main_menu import MainMenu
        self.pack_forget()
        MainMenu(self.master).pack()
