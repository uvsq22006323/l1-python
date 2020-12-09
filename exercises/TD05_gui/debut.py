import tkinter as tk
# from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

# Retirer la condition
# if __name__ == '__main__':
# et remplacer la fonction canvas.pack() par la fonction de positionnement
# des widgets que l'on a vue en cours. Puis testez votre programme.



if __name__ == '__main__':
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
    canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

    canvas.pack()
    root.mainloop()


# 2
# Le code va créer ine ligne avec 3 cercles ; un à chaque bout et un au milieu
