# Fonction pour ouvrir la calculatrice
def ouvrir_calculatrice():
    def ajouter_caractere(caractere):
        expression.set(expression.get() + str(caractere))

    def calculer():
        resultat.set(eval(expression.get()))

    fenetre_calculatrice = tk.Toplevel(root)
    fenetre_calculatrice.title("Calculatrice")
    expression = tk.StringVar()
    resultat = tk.StringVar()
    expression_entry = tk.Entry(fenetre_calculatrice, textvariable=expression)
    expression_entry.grid(row=0, column=0, columnspan=4)
    boutons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
    ]
    for (texte, ligne, colonne) in boutons:
        bouton = tk.Button(fenetre_calculatrice, text=texte, command=lambda t=texte: ajouter_caractere(t))
        bouton.grid(row=ligne, column=colonne)
    bouton_calculer = tk.Button(fenetre_calculatrice, text="=", command=calculer)
    bouton_calculer.grid(row=5, column=0, columnspan=4)
    resultat_label = tk.Label(fenetre_calculatrice, textvariable=resultat)
    resultat_label.grid(row=6, column=0, columnspan=4)
