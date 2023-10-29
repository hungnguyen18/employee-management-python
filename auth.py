import customtkinter
import tkinter.messagebox as messagebox
import pyrebase

tk = customtkinter

firebaseConfig = {
    "apiKey": "AIzaSyAlUWRF3ISCOGlB2KLftbKO7-1e1x2atuU",
    "authDomain": "py-auth-2eff3.firebaseapp.com",
    "databaseURL": "https://py-auth-2eff3-default-rtdb.firebaseio.com",
    "projectId": "py-auth-2eff3",
    "storageBucket": "py-auth-2eff3.appspot.com",
    "messagingSenderId": "8507796776",
    "appId": "1:8507796776:web:173400486f1e9e4ac8b41d",
    "measurementId": "G-V9KH2XTHVQ",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class AuthScreen:
    def __init__(self, master, success_callback):
        self.master = master
        self.success_callback = success_callback

        self.username_label = tk.CTkLabel(
            master=self.master,
            text="Username",
            width=80,
            height=35,
            text_color="black",
            corner_radius=10,
            fg_color=("black", "white"),
        )
        self.username_label.place(relx=0.4, rely=0.3, anchor=tk.CENTER)
        self.username_entry = tk.CTkEntry(
            master=self.master,
            placeholder_text="Username",
            width=250,
            height=35,
            border_width=2,
            corner_radius=10,
        )
        self.username_entry.place(relx=0.55, rely=0.3, anchor=tk.CENTER)

        self.password_label = tk.CTkLabel(
            master=self.master,
            text="Password",
            width=80,
            height=35,
            text_color="black",
            corner_radius=10,
            fg_color=("black", "white"),
        )
        self.password_label.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
        self.password_entry = tk.CTkEntry(
            master=self.master,
            placeholder_text="Password",
            width=250,
            height=35,
            border_width=2,
            corner_radius=10,
        )
        self.password_entry.place(relx=0.55, rely=0.4, anchor=tk.CENTER)

        self.login_btn = tk.CTkButton(
            master=self.master,
            width=80,
            height=32,
            border_width=0,
            corner_radius=8,
            text="Login",
            command=self.login_task,
        )
        self.login_btn.place(relx=0.55, rely=0.5, anchor=tk.CENTER)

    def login_task(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        try:
            login = auth.sign_in_with_email_and_password(email, password)
            self.master.destroy()
            self.success_callback()

        except:
            messagebox.showerror(title="Login", message="Login failure")
