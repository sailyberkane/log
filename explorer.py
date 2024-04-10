# Fonction pour ouvrir un explorateur de fichiers
def ouvrir_explorateur_fichiers():
    fenetre_explorateur = tk.Toplevel(root)
    fenetre_explorateur.title("Explorateur de fichiers")
    scrollbar = tk.Scrollbar(fenetre_explorateur)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox = tk.Listbox(fenetre_explorateur, yscrollcommand=scrollbar.set)
    listbox.pack(expand=True, fill="both")
    scrollbar.config(command=listbox.yview)
    for fichier in os.listdir():
        listbox.insert(tk.END, fichier)
