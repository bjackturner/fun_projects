import tkinter as tk
from PIL import Image, ImageTk

path = "fun_projects/minecraft_gradient/default_textures/acacia_planks.png"

root = tk.Tk() # Create main window

root.title("Block Blend 2D") # Change the title of the window
root.minsize(500, 400) # Change the mininum screen size window can be
root.resizable(width=True, height=True)

block = ImageTk.PhotoImage(Image.open(path)) # PhotoImage = convert pillow object (Image = opens path)
panel = tk.Label(root, image = block)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()