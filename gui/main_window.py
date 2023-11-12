import tkinter as tk
from tkinter import messagebox
from src import password_generator
import pyperclip as cd
from data_base import main_bd


class PasswordGeneratorApp:

    def __init__(self, root=None):
        self.ready_password = []
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root,
                                     text="Choose Password Length 8, 12, 16:")
        self.length_entry = tk.Entry(root,
                                     width=5)
        self.generate_button = tk.Button(root, text="Generate password",
                                         command=self.generate_password)
        self.generate_button_plus_dash = tk.Button(root, text="Add dash",
                                                   command=self.add_dash)
        self.generate_button_plus_digit = tk.Button(root, text="Add digit",
                                                    command=self.add_digit)
        self.generate_button_lowercase_letter = tk.Button(root, text="Add lower letter",
                                                          command=self.add_lowercase_letter)
        self.generate_button_upper_letter = tk.Button(root, text="Add upper letter",
                                                      command=self.add_uppercase_letter)
        self.add_password_bd_func = tk.Button(root, text="DataBase",
                                              command=self.add_password_bd)
        self.copy_button_password = tk.Button(root, text="Copy password",
                                              command=self.copy_password)
        self.result_label = tk.Label(root, text="Generated Password:")

        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.generate_button_plus_dash.grid(row=4, column=0, columnspan=2, pady=10)
        self.generate_button_plus_digit.grid(row=5, column=0, columnspan=2, pady=10)
        self.generate_button_lowercase_letter.grid(row=6, column=0, columnspan=2, pady=10)
        self.generate_button_upper_letter.grid(row=7, column=0, columnspan=2, pady=10)
        self.add_password_bd_func.grid(row=8, column=0, columnspan=2, pady=10)
        self.copy_button_password.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length in [8, 12, 16]:
                self.ready_password = [password_generator.GeneratorsUsersPasswords().generator_password(length)]
                self.result_label.config(text=f"Generated Password: {''.join(self.ready_password)}")
            else:
                messagebox.showerror("Error", "Please enter a length 8, 12, 16")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")

    def copy_password(self):
        copy_pass = ''.join(self.ready_password)
        cd.copy(copy_pass)

    def show_password(self):
        self.result_label.config(text=f"Generated Password: {''.join(self.ready_password)}")

    def add_dash(self):
        self.ready_password.append(password_generator.GeneratorDash().get_dash())
        self.show_password()

    def add_digit(self):
        self.ready_password.append(password_generator.GeneratorDigit().get_generator_digit())
        self.show_password()

    def add_lowercase_letter(self):
        self.ready_password.append(password_generator.GeneratorLetters().get_lowercase_letters())
        self.show_password()

    def add_uppercase_letter(self):
        self.ready_password.append(password_generator.GeneratorLetters().get_uppercase_letters())
        self.show_password()

    def add_password_bd(self):
        return main_bd.insert_variable_into_table(''.join(self.ready_password))
