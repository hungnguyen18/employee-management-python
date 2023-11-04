import customtkinter
import tkinter.messagebox as messagebox

import database

tk = customtkinter
auth = database.firebase.auth()


class AuthScreen:
    def __init__(self, master, success_callback):
        self.master = master
        self.success_callback = success_callback

        self.username_label = tk.CTkLabel(
            master=self.master,
            text="Username",
            width=80,
            height=35,
        )
        self.username_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
        self.username_entry = tk.CTkEntry(
            master=self.master,
            placeholder_text="Username",
            width=250,
            height=35,
            border_width=2,
            corner_radius=10,
        )
        self.username_entry.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.password_label = tk.CTkLabel(
            master=self.master,
            text="Password",
            width=80,
            height=35,
        )
        self.password_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")
        self.password_entry = tk.CTkEntry(
            master=self.master,
            placeholder_text="Password",
            width=250,
            height=35,
            border_width=2,
            corner_radius=10,
            show="*",
        )
        self.password_entry.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.login_btn = tk.CTkButton(
            master=self.master,
            width=80,
            height=32,
            border_width=0,
            corner_radius=8,
            text="Login",
            command=self.login_task,
        )
        self.login_btn.grid(row=2, column=1, padx=20, pady=(20, 0), sticky="nsew")

    def login_task(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        try:
            login = auth.sign_in_with_email_and_password(email, password)
            self.master.destroy()
            self.success_callback()
            return
        except:
            messagebox.showerror(title="Login", message="Login failure")
            return
