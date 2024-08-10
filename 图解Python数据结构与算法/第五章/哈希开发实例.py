import hashlib
import tkinter as tk
from tkinter import messagebox

class PasswordManagerUI:
    def __init__(self, master):
        self.master = master
        master.title("哈希算法实例")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="e")

        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=1)

        self.store_button = tk.Button(master, text="Store Password", command=self.store_password)
        self.store_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.verify_button = tk.Button(master, text="Verify Password", command=self.verify_password)
        self.verify_button.grid(row=3, column=0, columnspan=2)

        self.password_manager = PasswordManager()

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def store_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)
        self.password_manager.store_password(username, hashed_password)
        messagebox.showinfo("Success", "Password for user '{}' stored successfully.".format(username))

    def verify_password(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = self.hash_password(password)
        self.password_manager.verify_password(username, hashed_password)

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def store_password(self, username, hashed_password):
        self.passwords[username] = hashed_password

    def verify_password(self, username, hashed_password):
        stored_password = self.passwords.get(username)
        if stored_password:
            if stored_password == hashed_password:
                messagebox.showinfo("Success", "Password for user '{}' is correct.".format(username))
            else:
                messagebox.showerror("Error", "Incorrect password for user '{}'.".format(username))
        else:
            messagebox.showerror("Error", "User '{}' not found.".format(username))

def main():
    root = tk.Tk()
    app = PasswordManagerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
