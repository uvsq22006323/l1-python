import tkinter as tk

# from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
W, H = 600, 400
# 3
# Besoin de fonction grid()

# 5
# Modifier le programme pour que la ligne qui s'affiche devienne verticale
# tout en conservant les cercles à ses extrémités.


racine = tk.Tk()
racine.title("Début TD 05")
canvas = tk.Canvas(racine, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.grid()


# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
x = CANVAS_WIDTH / 2

y1 = 100
y2 = CANVAS_HEIGHT - 100
y = CANVAS_HEIGHT / 2

# canvas.create_line(x0, y, x1, y)
# canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
# canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
# canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

canvas.create_line(x, y1, x, y2)
canvas.create_oval(x - 50, y1 - 50, x + 50, y1 + 50)
canvas.create_oval(x - 50, (y1 + y2) / 2 - 50, x + 50, (y1 + y2)/2 + 50)
canvas.create_oval(x - 50, y2 - 50, x + 50, y2 + 50)
# Fin de votre code

racine.mainloop()


# 2
# Le code va créer ine ligne avec 3 cercles ; un à chaque bout et un au milieu
