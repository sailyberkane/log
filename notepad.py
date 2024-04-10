# Fonction pour ouvrir Notepad
def ouvrir_notepad():
    fenetre_notepad = tk.Toplevel(root)
    fenetre_notepad.title("Notepad")
    text_area = tk.Text(fenetre_notepad)
    text_area.pack(expand=True, fill="both")
