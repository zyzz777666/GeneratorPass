from gui import main_window


if __name__ == "__main__":
    root = main_window.tk.Tk()
    app = main_window.PasswordGeneratorApp(root)
    root.mainloop()
