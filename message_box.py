from tkinter import messagebox


def message_box(callback_yes, callback_no):
    result = messagebox.askyesno("Confirmation", "Are you sure?")
    if result:
        print("User clicked Yes")
        callback_yes()
    else:
        print("User clicked No")
        callback_no()
