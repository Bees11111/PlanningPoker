import tkinter as tk
from backlog import EntrerBacklog

# Create the main window
root = tk.Tk()
root.title("Planning Poker")

# Set the background color to a nice blue
root.configure(bg="#008080")

root.geometry("1100x600")

# Create frames for the main menu, options menu, jouer menu, and tutorial menu
main_menu = EntrerBacklog(root)

# Show the main menu frame initially
main_menu.pack()

# Start the Tkinter event loop
root.mainloop()
