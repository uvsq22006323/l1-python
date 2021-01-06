import tkinter as tk

w = 500
h = 500

racine = tk.Tk()

racine.title("Cible de merde")


color = ["blue", "green", "black", "yellow", "magenta", "red"]


canvas = tk.Canvas(racine, width=w, height=h, background="black")
canvas.grid()

nb_cercles = 30

épaisseur = (w // 2) // nb_cercles

for i in range(nb_cercles):
    canvas.create_oval(i * épaisseur, i * épaisseur,
                        w - i * épaisseur, h - i * épaisseur,
                        fill=color[i % len(color)], width=0)


# dessiner un cercle

# variables = taille, couleur
# dire combien on veut de cycles dedans

# colorer le cercle sans s'arrêter ou butter sur une couleur

# blue, green, black, yellow, magenta, red

racine.mainloop()
