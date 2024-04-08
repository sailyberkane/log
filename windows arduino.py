import tkinter as tk
from tkinter import ttk
import os
import subprocess
import datetime

# Fonction pour ouvrir Notepad
def ouvrir_notepad():
    fenetre_notepad = tk.Toplevel(root)
    fenetre_notepad.title("Notepad")
    text_area = tk.Text(fenetre_notepad)
    text_area.pack(expand=True, fill="both")

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

# Fonction pour ouvrir le traitement de texte
def ouvrir_traitement_texte():
    fenetre_traitement_texte = tk.Toplevel(root)
    fenetre_traitement_texte.title("Traitement de texte")
    text_area = tk.Text(fenetre_traitement_texte)
    text_area.pack(expand=True, fill="both")

# Fonction pour ouvrir Paint
def ouvrir_paint():
    def dessiner(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canevas.create_oval(x1, y1, x2, y2, fill="black", width=2)

    fenetre_paint = tk.Toplevel(root)
    fenetre_paint.title("Paint")
    canevas = tk.Canvas(fenetre_paint, bg="white", width=400, height=400)
    canevas.pack()
    canevas.bind("<B1-Motion>", dessiner)

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

# Fonction pour ouvrir le lecteur multimédia intégré à Windows
def ouvrir_lecteur_multimedia():
    os.system("start wmplayer")

# Fonction pour afficher le calendrier
def afficher_calendrier():
    fenetre_calendrier = tk.Toplevel(root)
    fenetre_calendrier.title("Calendrier")
    aujourd_hui = datetime.datetime.now()
    mois = tk.Label(fenetre_calendrier, text=aujourd_hui.strftime("%B %Y"), font=("Arial", 12))
    mois.pack()
    calendrier = tk.Text(fenetre_calendrier, height=6, width=20)
    calendrier.pack()
    calendrier.insert(tk.END, aujourd_hui.strftime("%A\n%d %B %Y"))

# Fonction pour ouvrir une liste de mots déroulante
def afficher_liste_mots():
    fenetre_liste = tk.Toplevel(root)
    fenetre_liste.title("Liste de Mots")
    liste_mots = ["Mot 1", "Mot 2", "Mot 3", "Mot 4", "Mot 5"]
    combo = ttk.Combobox(fenetre_liste, values=liste_mots)
    combo.pack(padx=20, pady=20)

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
    fenetre_navigateur.title("Navigateur de Fichiers Texte")

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

# Fonction pour afficher la barre de tâche personnalisée
def afficher_barre_tache():
    barre_tache = tk.Label(root, text="", bg="blue", fg="white", height=2, anchor="w")
    barre_tache.grid(row=4, column=0, columnspan=10, sticky="ew")

    # Ajouter le bouton "Lista" à gauche de la barre de tâche
    btn_lista = tk.Button(barre_tache, text="Démarée", command=afficher_liste_mots)
    btn_lista.grid(row=0, column=0, padx=5, pady=5)

    # Ajouter les boutons pour chaque programme
    boutons_programmes = [
        ("Notepad", ouvrir_notepad), 
        ("Calculatrice", ouvrir_calculatrice), 
        ("Traitement de texte", ouvrir_traitement_texte), 
        ("Paint", ouvrir_paint), 
        ("Explorateur de fichiers", ouvrir_explorateur_fichiers), 
        ("Lecteur multimédia", ouvrir_lecteur_multimedia), 
        ("Calendrier", afficher_calendrier),
        ("Navigateur de fichiers texte", ouvrir_navigateur_fichiers_texte)
    ]

    for i, (nom_programme, commande_programme) in enumerate(boutons_programmes, start=1):
        btn_programme = tk.Button(barre_tache, text=nom_programme, command=commande_programme)
        btn_programme.grid(row=0, column=i, padx=5, pady=5)

# Création de la fenêtre principale
root = tk.Tk()
root.title("MicroArd - Windows Arduino")

# Division de la fenêtre principale en quatre parties égales avec une croix
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Affichage de la barre de tâche personnalisée
afficher_barre_tache()

# Lancement de la boucle principale
root.mainloop()
