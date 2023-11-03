import customtkinter
from tkinter import ttk
import database
import create_entry
from message_box import message_box

namespace = "employees"
ctk = customtkinter
db = database.firebase.database()


class Employees:
    def __init__(self, master, tab_view):
        self.master = master
        self.tab_view = tab_view

        self.id_val = ctk.StringVar()
        self.id_entry = create_entry.create_entry_with_label(
            tab_view,
            1,
            "Id:",
            "Id",
            self.id_val,
            "disabled",
        )

        self.clear_button = ctk.CTkButton(
            tab_view,
            width=200,
            text="Clear fields",
            command=lambda: self.clear_entry_fields(),
        )
        self.clear_button.grid(
            row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew"
        )

        self.name_val = ctk.StringVar()
        self.name_entry = create_entry.create_entry_with_label(
            tab_view, 2, "Name:", "Name", self.name_val
        )

        self.phone_val = ctk.StringVar()
        self.phone_entry = create_entry.create_entry_with_label(
            tab_view, 3, "Phone:", "Phone", self.phone_val
        )

        self.salary_val = ctk.StringVar()
        self.salary_entry = create_entry.create_entry_with_label(
            tab_view, 4, "Salary:", "Salary", self.salary_val
        )

        self.department_val = ctk.StringVar()
        self.department_entry = create_entry.create_entry_with_label(
            tab_view, 5, "Department:", "Department", self.department_val
        )

        self.create_button = ctk.CTkButton(
            tab_view,
            width=200,
            text="Create",
            fg_color="green",
            command=lambda: self.insert(),
        )
        self.create_button.grid(row=6, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.update_button = ctk.CTkButton(
            tab_view, width=200, text="Update", command=lambda: self.update()
        )
        self.update_button.grid(row=6, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.remove_button = ctk.CTkButton(
            tab_view,
            width=200,
            text="Remove",
            fg_color="red",
            command=lambda: self.remove(),
        )
        self.remove_button.grid(row=7, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.filter_button = ctk.CTkButton(
            tab_view, width=200, text="Filter", command=lambda: self.clear_tree()
        )
        self.filter_button.grid(row=7, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.import_button = ctk.CTkButton(tab_view, width=200, text="Import")
        self.import_button.grid(row=8, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.export_button = ctk.CTkButton(tab_view, width=200, text="Export")
        self.export_button.grid(row=8, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.headings = [
            "Id",
            "Name",
            "Phone",
            "Salary",
            "Department",
        ]

        self.tree = ttk.Treeview(
            tab_view,
            columns=self.headings,
            show="headings",
            height=100,
        )
        for heading in self.headings:
            self.tree.heading(heading, text=heading)

        self.populate_treeview()

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                value = item["values"]
                print(value)
                self.id_val.set(value[0])
                self.name_val.set(value[1])
                self.phone_val.set(value[2])
                self.salary_val.set(value[3])
                self.department_val.set(value[4])

        self.tree.bind("<<TreeviewSelect>>", item_selected)
        self.tree.grid(row=0, column=2, rowspan=100)

    def get(self):
        result = []
        employees = db.child(namespace).get()
        print(employees)
        if not employees:
            return result
        for employee in employees.each():
            print(employee.val())
            result.append(
                (
                    employee.key(),
                    employee.val()["name"],
                    employee.val()["phone"],
                    employee.val()["salary"],
                    employee.val()["department"],
                )
            )

        return result

    def insert(self):
        index = str(len(self.get())) if self.get() else "1"
        data = {
            "id": index,
            "name": self.name_entry.get(),
            "phone": self.phone_entry.get(),
            "salary": self.salary_entry.get(),
            "department": self.department_entry.get(),
        }
        db.child(namespace).child(index).set(data)
        self.populate_treeview()

    def update(self):
        data = {
            "id": self.id_entry.get(),
            "name": self.name_entry.get(),
            "phone": self.phone_entry.get(),
            "salary": self.salary_entry.get(),
            "department": self.department_entry.get(),
        }
        db.child(namespace).child(data["id"]).update(data)
        self.populate_treeview()

    def remove(self):
        def confirm():
            db.child(namespace).child(self.id_entry.get()).remove()
            self.clear_entry_fields()
            self.populate_treeview()

        def cancel():
            print("Cancel")

        message_box(confirm, cancel)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for item in self.get():
            self.tree.insert("", ctk.END, values=item)

    def clear_entry_fields(self):
        self.id_val.set("")
        self.name_val.set("")
        self.phone_val.set("")
        self.salary_val.set("")
        self.department_val.set("")
