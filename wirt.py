# Fonction pour ouvrir le traitement de texte
def ouvrir_traitement_texte():
    fenetre_traitement_texte = tk.Toplevel(root)
    fenetre_traitement_texte.title("Traitement de texte")
    text_area = tk.Text(fenetre_traitement_texte)
    text_area.pack(expand=True, fill="both")
