import tkinter as tk
from tkinter import messagebox
from src import password_generator


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Choose Password Length 4, 8, 12, 16:")
        self.length_entry = tk.Entry(root, width=5)
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.result_label = tk.Label(root, text="Generated Password:")

        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length in [4, 8, 12, 16]:
                password = password_generator.GeneratorsUsersPasswords().generator_password(length)
                self.result_label.config(text=f"Generated Password: {password}")
            else:
                messagebox.showerror("Error", "Please enter a length 4, 8, 12, 16")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")
