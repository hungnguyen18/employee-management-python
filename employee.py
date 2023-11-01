import customtkinter

tk = customtkinter


class Employees:
    def __init__(self, master, tabView):
        self.master = master
        self.tabView = tabView

        self.button_1 = tk.CTkButton(self.tabView)
        self.button_1.pack(padx=20, pady=20)
