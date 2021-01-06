import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Mon dessin")


w = 600
h = 600


def draw_circle():
    centre_x = rd.randint(50, w - 50)
    centre_y = rd.randint(50, h - 50)

    identifiant = mon_canvas.create_oval(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill=couleur_courante)
    objets.append(identifiant)


def draw_square():
    centre_x = rd.randint(50, w - 50)
    centre_y = rd.randint(50, h - 50)

    identifiant = mon_canvas.create_rectangle(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill=couleur_courante)
    objets.append(identifiant)


def draw_cross():
    centre_x = rd.randint(50, w - 50)
    centre_y = rd.randint(50, h - 50)

    identifiant = mon_canvas.create_line(centre_x, centre_y - 50, centre_x, centre_y + 50, fill=couleur_courante)
    identifiant = mon_canvas.create_line(centre_x - 50, centre_y, centre_x + 50, centre_y, fill=couleur_courante)
    objets.append(identifiant)


def choix_couleur():
    global couleur_courante
    couleur_courante = input("Donnez une couleur svp\n")


# def Undo():
#   if len(objets) != 0:
#       mon_canvas.delete(objets[-1])
#       del objets[-1]


couleur_courante = "blue"
objets = []

couleur = tk.Button(racine, text="Choisir une couleur", bg="red", command=choix_couleur)
cercle = tk.Button(racine, text="Cercle", command=draw_circle)
carré = tk.Button(racine, text="Carré", command=draw_square)
croix = tk.Button(racine, text="Croix", backgroung="blue", foregroung="red", activebackground="yellow", activeforeground="black", pady=10, font=("helvetica", 26), command=draw_cross)

# undo = tk.Button(racine, text="Undo", command=Undo)

mon_canvas = tk.Canvas(racine, width=w, height=h, background="black", borderwidth=5, relief="raised")


couleur.grid(row=0, column=1)
cercle.grid(row=1, column=0)
carré.grid(row=2, column=0)
croix.grid(row=3, column=0)
# undo.grid(row=0, column=2)

mon_canvas.grid(row=1, rowspan=3, column=1, columnspan=2)

racine.mainloop()
