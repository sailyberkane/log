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
