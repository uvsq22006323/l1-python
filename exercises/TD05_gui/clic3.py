import tkinter as tk


nb_clic = 0
point1_x = -1
point1_y = -1


def draw_line(event):
    global point1_x, point1_y, nb_clic
    if nb_clic == 0:
        point1_x, point1_y = event.x, event.y
        nb_clic += 1
    else:
        if (point1_x < W/2 and event.x < W/2) \
            or (point1_x > W/2 and event.X > W/2):
            couleur = "blue"
        else:
            couleur = "red"
        mon_canvas.create_line(point1_x, point1_y, event.x, event.y, fill=couleur, width=4)


racine = tk.Tk()
W = 500
H = 500
mon_canvas = tk.Canvas(racine, background="black", width=W, height=H)
mon_canvas.grid()


mon_canvas.create_line(W/2, 0, W/2, H, fill="white")


mon_canvas.bind("<Button-1>", draw_line)


racine.mainloop()
