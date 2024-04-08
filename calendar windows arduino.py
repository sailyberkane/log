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
