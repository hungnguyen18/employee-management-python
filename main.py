import customtkinter
from auth import AuthScreen
from employee import Employees
from department import Department
from chart import draw_chart

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
        Department(self.master, self.tabView.tab("Department"))
        # draw_chart()

    def show(self):
        self.master.mainloop()


def login_success_callback():
    global main_screen
    app = tk.CTk()
    app.geometry("1500x800")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    main_screen = MainScreen(app)
    main_screen.show()


if __name__ == "__main__":
    app = tk.CTk()
    # Get the screen width and height
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # Calculate the x and y coordinates for the centered window
    x = (screen_width // 2) - (400 // 2)  # Width of the window is set to 400
    y = (screen_height // 2) - (200 // 2)  # Height of the window is set to 200
    app.geometry(f"400x200+{x}+{y}")
    app.title = "LOGIN"
    auth_screen = AuthScreen(app, login_success_callback)
    app.mainloop()
    # login_success_callback()
