import customtkinter
from auth import AuthScreen
from employee import Employees

tk = customtkinter
main_screen = None


class MainScreen:
    def __init__(self, master):
        self.master = master
        # TODO: Xây dựng giao diện màn hình chính ở đây
        self.tabView = tk.CTkTabview(self.master, height=700)
        self.tabView.pack(
            padx=20,
            pady=20,
            fill=tk.BOTH,
        )
        self.tabView.add("Employees")
        self.tabView.add("Department")

        Employees(self.master, self.tabView.tab("Employees"))

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
