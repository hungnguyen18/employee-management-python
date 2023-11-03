import csv
import customtkinter

ctk = customtkinter


def export_to_csv(data):
    input_dialog = ctk.CTkInputDialog(text="File csv name", title="Export")
    with open(f"{input_dialog.get_input()}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
