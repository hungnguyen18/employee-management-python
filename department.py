import customtkinter
from tkinter import ttk
import database
import create_entry
from message_box import message_box
import tkinter.messagebox as messagebox
from export_csv import export_to_csv
from import_csv import import_from_csv, open_file_dialog


namespace = "departments"
ctk = customtkinter
db = database.firebase.database()


class Department:
    def __init__(self, master, tab_view):
        self.master = master
        self.tab_view = tab_view
        self.options = []

        self.clear_button = ctk.CTkButton(
            tab_view,
            width=200,
            text="Clear fields",
            command=lambda: self.clear_entry_fields(),
        )
        self.clear_button.grid(
            row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew"
        )

        self.filter_button = ctk.CTkLabel(tab_view, text="Filter:")
        self.filter_button.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")
        self.filter_button = ctk.CTkOptionMenu(
            tab_view, values=self.get_options(), command=self.optionmenu_callback
        )
        self.filter_button.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.id_label = ctk.CTkLabel(tab_view, text="ID:")
        self.id_label.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="w")

        self.id_val = ctk.StringVar()
        self.id_entry = ctk.CTkLabel(tab_view, textvariable=self.id_val)
        self.id_entry.grid(row=2, column=1)

        self.idx_val = ctk.StringVar()
        self.idx_entry = create_entry.create_entry_with_label(
            tab_view, 3, "Index(disabled):", "Index", self.idx_val, state="disabled"
        )

        self.name_val = ctk.StringVar()
        self.name_entry = create_entry.create_entry_with_label(
            tab_view, 4, "Name:", "Name", self.name_val
        )

        self.create_button = ctk.CTkButton(
            tab_view,
            width=200,
            text="Create",
            fg_color="green",
            command=lambda: self.insert(),
        )
        self.create_button.grid(row=8, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.update_button = ctk.CTkButton(
            tab_view, width=200, text="Update", command=lambda: self.update()
        )
        self.update_button.grid(row=8, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.remove_button = ctk.CTkButton(
            tab_view,
            width=200,
            text="Remove",
            fg_color="red",
            command=lambda: self.remove(),
        )
        self.remove_button.grid(row=9, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.reload_button = ctk.CTkButton(
            tab_view, width=200, text="Reload", command=lambda: self.populate_treeview()
        )
        self.reload_button.grid(row=9, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.import_button = ctk.CTkButton(
            tab_view, width=200, text="Import", command=lambda: self.import_data()
        )
        self.import_button.grid(row=10, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.export_button = ctk.CTkButton(
            tab_view, width=200, text="Export", command=lambda: self.export()
        )
        self.export_button.grid(row=10, column=1, padx=20, pady=(20, 0), sticky="nsew")

        self.headings = [
            "Id",
            "Name",
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
                self.idx_val.set(value[0])
                self.id_val.set(value[2])
                self.name_val.set(value[1])

        self.tree.bind("<<TreeviewSelect>>", item_selected)
        self.tree.grid(row=0, column=2, rowspan=100)

    def get(self):
        try:
            result = []
            employees = db.child(namespace).get()
            for employee in employees.each():
                emp_data = employee.val()
                emp_tuple = (
                    emp_data.get("id"),
                    emp_data.get("name"),
                    employee.key(),
                )
                result.append(emp_tuple)
                self.options.append(emp_data.get("department"))
            return result
        except Exception as e:
            print("An error occurred:", str(e))
            return []

    def insert(self):
        index = str(len(self.get()) + 1) if self.get() else "1"
        data = {
            "id": index,
            "name": self.name_entry.get(),
        }
        try:
            db.child(namespace).push(data)
            self.populate_treeview()
            messagebox.showinfo(title="Successfully", message="Insert Successfully")
        except:
            messagebox.showerror(title="Fail", message="Insert failed")

    def update(self):
        data = {
            "id": self.idx_entry.get(),
            "name": self.name_entry.get(),
        }
        try:
            db.child(namespace).child(self.id_val.get()).update(data)
            self.populate_treeview()
            messagebox.showinfo(title="Successfully", message="Update Successfully")
        except:
            messagebox.showerror(title="Fail", message="Update failed")

    def remove(self):
        def confirm():
            db.child(namespace).child(self.id_val.get()).remove()
            self.clear_entry_fields()
            self.populate_treeview()

        def cancel():
            print("Cancel")

        message_box(confirm, cancel)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for item in self.get():
            self.tree.insert("", ctk.END, values=item)
        self.get_options()

    def export(self):
        reduce_data = [(tup[:-1]) for tup in self.get()]
        self.data = [self.headings] + [list(item) for item in reduce_data]
        try:
            export_to_csv(self.data)
            messagebox.showinfo(title="Successfully", message="Export Successfully")
        except:
            messagebox.showerror(title="Fail", message="Export failed")

    def import_data(self):
        # Example usage
        file_path = open_file_dialog()
        if file_path:
            data = import_from_csv(file_path)
            print("Imported data:", data)
            keys = [key.lower() for key in data[0]]
            result = [
                {keys[i]: value for i, value in enumerate(row)} for row in data[1:]
            ]
            db.child(namespace).remove()
            for item in result:
                db.child(namespace).push(item)

            self.populate_treeview()

            messagebox.showinfo(title="Successfully", message="Import Successfully")
        else:
            print("No file selected.")

    def get_options(self):
        crop_key = [item[1] for item in self.get()]
        return list(set(crop_key))

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)
        filtered_keys = [item for item in self.get() if item[1] == choice]
        self.tree.delete(*self.tree.get_children())
        for item in filtered_keys:
            self.tree.insert("", ctk.END, values=item)

    def clear_entry_fields(self):
        self.idx_val.set("")
        self.id_val.set("")
        self.name_val.set("")
