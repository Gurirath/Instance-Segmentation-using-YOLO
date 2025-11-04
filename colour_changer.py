import tkinter as tk
from tkinter import colorchooser

class ColorChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Changing Interface")
        self.root.geometry("400x300")
        
        # Label to show instructions
        self.label = tk.Label(root, text="Choose a color to change background:", font=("Arial", 14))
        self.label.pack(pady=20)

        # Frame to hold buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Predefined Color Buttons
        colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
        for color in colors:
            btn = tk.Button(self.button_frame, bg=color, width=10, command=lambda c=color: self.change_color(c))
            btn.pack(side='left', padx=5)

        # Custom color chooser button
        self.custom_color_btn = tk.Button(root, text="Choose Custom Color", command=self.choose_custom_color)
        self.custom_color_btn.pack(pady=20)

    def change_color(self, color):
        self.root.config(bg=color)

    def choose_custom_color(self):
        # Open color chooser dialog
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1]:  # color_code[1] returns color in hex format, e.g., #ff0000
            self.change_color(color_code[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorChangerApp(root)
    root.mainloop()
