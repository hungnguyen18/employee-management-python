import tkinter
import customtkinter
from auth import AuthScreen

tk = customtkinter
main_screen = None


class MainScreen:
    def __init__(self, master):
        self.master = master

        # TODO: Xây dựng giao diện màn hình chính ở đây

    def show(self):
        self.master.mainloop()


def login_success_callback():
    global main_screen
    app = tk.CTk()
    app.geometry("1280x720")
    main_screen = MainScreen(app)
    main_screen.show()


if __name__ == "__main__":
    app = tk.CTk()
    app.geometry("800x600")
    auth_screen = AuthScreen(app, login_success_callback)
    app.mainloop()
