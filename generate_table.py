import tkinter.ttk as ttk
from tkinter import messagebox


def create_treeview(tabView):
    headings = [
        "Id",
        "Name",
        "Phone",
        "Salary",
        "Department",
    ]
    data = []
    for n in range(1, 100):
        data.append((f"number {n}", f"name {n}", f"number {n}", n, n))
    tree = ttk.Treeview(tabView, columns=headings, show="headings")

    # Define headings
    tree.heading("Id", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone Number")
    tree.heading("Salary", text="Salary")
    tree.heading("Department", text="Department")
    tree.grid(row=0, column=2, rowspan=6)

    # Add data to the treeview
    for contact in data:
        tree.insert("", "end", values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item["values"]
            # Show a message
            messagebox.showinfo(title="Information", message=",".join(record))

    tree.bind("<<TreeviewSelect>>", item_selected)

    return tree
