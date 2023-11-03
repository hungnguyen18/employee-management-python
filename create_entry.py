import customtkinter

ctk = customtkinter


def create_entry_with_label(
    root, row, label_text, placeholder_text, textvariable, state="normal"
):
    label = ctk.CTkLabel(root, text=label_text)
    label.grid(row=row, column=0, padx=20, pady=(20, 0), sticky="w")

    entry = ctk.CTkEntry(
        root,
        placeholder_text=placeholder_text,
        width=200,
        textvariable=textvariable,
        state=state,
    )
    entry.grid(row=row, column=1, padx=20, pady=(20, 0), sticky="nsew")
    return entry
