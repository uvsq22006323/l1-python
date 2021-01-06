import tkinter as tk

racine = tk.Tk()
racine.title("Truc")


aléa = tk.Button(racine, text="Aléatoire")
aléa.grid(row=0, column=0)

gris = tk.Button(racine, text="Dégradé gris")
gris.grid(row=1, column=0)

D_2 = tk.Button(racine, text="Dégradé 2D")
D_2.grid(row=2, column=0)

canvas = tk.Canvas(racine, width=256, height=256, background="black")
canvas.grid(row=0, rowspan=3, column=1)

# def get_color(r, g, b):
#   """ Retourne une couleur à partir de ses composantes r, g, b entre
#   0 et 255"""
#   return '#{:02x}{:02x}{:02x}'.format(r, g, b)


# 2
# Écrire la fonction def draw_pixel(i, j, color) qui colorie le pixel (i, j)
# du canvas de la couleur color. La tester en allumant en blanc le pixel du
# milieu du canevas.

# def draw_pixel(i, j, color):
#   """Colorie pixel (i, j) de la couleur color"""





racine.mainloop()
