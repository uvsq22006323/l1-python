import tkinter as tk

# Dans le fichier clic1.py, créer une fenêtre graphique qui contient un
# canevas de taille 500x500 et de couleur noire. Quand on clique sur le canevas
# un pixel de couleur rouge s'affiche à l'endroit où l'on a cliqué.


# Copier le contenu du fichier clic1.py dans le fichier clic2.py. Modifier le
# fichier
# clic2.py de manière à faire les choses suivantes:
#         afficher une ligne verticale en blanc qui sépare l'écran en 2
# parties égales
#       si l'utilisateur clique à gauche de la ligne afficher
# un cercle bleu et s'il est
#           à droite, afficher un cercle rouge. Dans les deux cas, le cercle
# sera centré là où l
#              utilisateur a cliqué. Le rayon du cercle est 50.


# 1
def dessine_cercle(event):
    coordonee_x = event.x
    coordonee_y = event.y
    couleur = ""
    if coordonee_x <= W/2:
        couleur = "blue"
    else:
        couleur = "red"
    mon_canvas.create_oval(coordonee_x-50, coordonee_y-50, coordonee_x+50, coordonee_y+50, fill=couleur)


racine = tk.Tk()
W = 500
H = 500
mon_canvas = tk.Canvas(racine, background="black", width=W, height=H)
mon_canvas.grid()


mon_canvas.create_line(W/2, 0, W/2, H, fill="white")


mon_canvas.bind("<Button-1>", dessine_cercle)


racine.mainloop()
