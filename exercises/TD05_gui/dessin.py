import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Mon dessin")


w = 600
h = 600


def draw_circle():
    centre_x = rd.randint(50, w - 50)
    centre_y = rd.randint(50, h - 50)

    mon_canvas.create_oval(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill=couleur_courante)


def draw_square():
    centre_x = rd.randint(50, w - 50)
    centre_y = rd.randint(50, h - 50)

    mon_canvas.create_rectangle(centre_x - 50, centre_y - 50, centre_x + 50, centre_y + 50, fill=couleur_courante)


def draw_cross():
    centre_x = rd.randint(50, w - 50)
    centre_y = rd.randint(50, h - 50)

    mon_canvas.create_line(centre_x, centre_y - 50, centre_x, centre_y + 50, fill=couleur_courante)
    mon_canvas.create_line(centre_x - 50, centre_y, centre_x + 50, centre_y, fill=couleur_courante)


def choix_couleur():
    global couleur_courante
    couleur_courante = input("Donnez une couleur svp\n")


couleur = tk.Button(racine, text="Choisir une couleur", bg="red", command=choix_couleur)
cercle = tk.Button(racine, text="Cercle", command=draw_circle)
carré = tk.Button(racine, text="Carré", command=draw_square)
croix = tk.Button(racine, text="Croix", backgroung="blue", foregroung="red",\
    activebackground="yellow", activeforeground="black", pady=10, font=("helvetica", 26), commend=draw_cross)


mon_canvas = tk.Canvas(racine, width=w, height=h, background="black", borderwidth=5, relief="raised")
mon_canvas.grid(row=1, rowspan=3, column=1)

couleur.grid(row=0, column=1)
cercle.grid(row=1, column=0)
carré.grid(row=2, column=0)
croix.grid(row=3, column=0)

racine.mainloop()

# 2
# Modifier le style par défaut des boutons, par exemple, en modifiant les
# couleurs, en ajoutant des marges, en changeant la taille de la police. Pour
# savoir ce qu'il est possible de faire, consultez le site indiqué au début du
# sujet
