import pyrebase
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")


def main():
    tk = customtkinter
    app = tk.CTk()
    app.geometry("800x600")

    username = tk.CTkLabel(
        master=app,
        text="Username",
        width=80,
        height=25,
        text_color="black",
        corner_radius=10,
        fg_color=("black", "white"),
    )
    username.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
    username_entry = tk.CTkEntry(
        master=app,
        placeholder_text="Username",
        width=180,
        height=35,
        border_width=2,
        corner_radius=10,
    )
    username_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    password = tk.CTkLabel(
        master=app,
        text="Password",
        width=80,
        height=25,
        text_color="black",
        corner_radius=10,
        fg_color=("black", "white"),
    )
    password.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
    password_entry = tk.CTkEntry(
        master=app,
        placeholder_text="Username",
        width=180,
        height=35,
        border_width=2,
        corner_radius=10,
    )
    password_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    app.mainloop()


if __name__ == "__main__":
    main()
