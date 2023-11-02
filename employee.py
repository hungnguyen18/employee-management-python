import customtkinter
from tkinter import ttk


ctk = customtkinter


class Employees:
    def __init__(self, master, tabView):
        self.master = master
        self.tabView = tabView

        self.id_entry = ctk.CTkEntry(tabView, placeholder_text="Id", width=100)
        self.id_entry.grid(
            row=0, column=0, padx=20, columnspan=2, pady=(20, 0), sticky="nsew"
        )

        self.name_entry = ctk.CTkEntry(tabView, placeholder_text="Name", width=100)
        self.name_entry.grid(
            row=1, column=0, padx=20, columnspan=2, pady=(20, 0), sticky="nsew"
        )

        self.phone_entry = ctk.CTkEntry(tabView, placeholder_text="Phone", width=100)
        self.phone_entry.grid(
            row=2, column=0, padx=20, columnspan=2, pady=(20, 0), sticky="nsew"
        )

        self.salary_entry = ctk.CTkEntry(tabView, placeholder_text="Salary", width=100)
        self.salary_entry.grid(
            row=3, column=0, padx=20, columnspan=2, pady=(20, 0), sticky="nsew"
        )

        self.department_entry = ctk.CTkEntry(
            tabView, placeholder_text="Department", width=100
        )
        self.department_entry.grid(
            row=4, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew"
        )

        self.filter = ctk.CTkButton(tabView, width=50, text="Filter")
        self.filter.grid(row=5, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.export = ctk.CTkButton(tabView, width=50, text="Export")
        self.export.grid(row=5, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.create = ctk.CTkButton(tabView, width=50, text="Create")
        self.create.grid(row=6, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.update = ctk.CTkButton(tabView, width=50, text="Update")
        self.update.grid(row=6, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.headings = [
            "Id",
            "Name",
            "Phone",
            "Salary",
            "Department",
        ]

        self.tree = ttk.Treeview(tabView, columns=self.headings, show="headings")
        # define headings
        self.tree.heading("Id", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.heading("Salary", text="Salary")
        self.tree.heading("Department", text="Department")

        # generate sample data
        self.data = []
        for n in range(1, 100):
            self.data.append((f"number {n}", f"name {n}", f"number {n}", n, n))
        # add data to the treeview
        for contact in self.data:
            print(contact)
            self.tree.insert("", ctk.END, values=contact)

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                value = item["values"]
                print(value)

        self.tree.bind("<<TreeviewSelect>>", item_selected)
        self.tree.grid(row=0, column=2, rowspan=6)
