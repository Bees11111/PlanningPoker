import tkinter as tk
from main_menu import MainMenu

# Create the main window
root = tk.Tk()
root.title("Planning Poker")

# Set the background color to a nice blue
root.configure(bg="#3498db")

# Set minimum window size
root.minsize(800, 500)

# Create frames for the main menu, options menu, jouer menu, and tutorial menu
main_menu = MainMenu(root)

# Show the main menu frame initially
main_menu.pack()

# Start the Tkinter event loop
root.mainloop()
