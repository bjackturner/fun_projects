import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Minecraft Block Display")
    root.geometry("400x400")  # Set the size of the window

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    # Call the function to display a block
    display_block(canvas, "stone")  # Change to "stone" to display a stone block

    root.mainloop()

def display_block(canvas, block_type):
    if block_type == "grass":
        color = "#4caf50"  # A green color for grass
    elif block_type == "stone":
        color = "#8b8b83"  # A gray color for stone
    else:
        return

    # Draw a square to represent the block
    canvas.create_rectangle(50, 50, 250, 250, fill=color, outline="")

if __name__ == "__main__":
    main()
