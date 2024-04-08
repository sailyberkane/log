# Fonction pour ouvrir un navigateur de fichiers texte
def ouvrir_navigateur_fichiers_texte():
    def afficher_contenu():
        chemin = entry_chemin.get()
        try:
            with open(chemin, 'r') as fichier:
                contenu.delete('1.0', tk.END)
                contenu.insert(tk.END, fichier.read())
        except FileNotFoundError:
            contenu.delete('1.0', tk.END)
            contenu.insert(tk.END, "Fichier introuvable!")

    fenetre_navigateur = tk.Toplevel(root)
    fenetre_navigateur.title("Ethernet explorer")

    # Barre d'adresse
    frame_adresse = tk.Frame(fenetre_navigateur)
    frame_adresse.pack(fill="x")
    tk.Label(frame_adresse, text="Chemin d'accès:").pack(side="left")
    entry_chemin = tk.Entry(frame_adresse, width=200)
    entry_chemin.pack(side="left")
    tk.Button(frame_adresse, text="Go", command=afficher_contenu).pack(side="left")

    # Séparateur gris
    separateur = ttk.Separator(fenetre_navigateur, orient='horizontal')
    separateur.pack(fill='x', padx=5, pady=5)

    # Contenu du fichier texte
    contenu = tk.Text(fenetre_navigateur, height=20, width=80)
    contenu.pack(fill="both", expand=True)
