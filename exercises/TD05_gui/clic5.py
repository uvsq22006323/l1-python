import tkinter as tk


nb_clic = 0
cercles = []


def gerer_cercle(event):
    global nb_clic
    nb_clic += 1
    if nb_clic < 9:
        identifiant = mon_canvas.create_oval(event.x-50, event.y-50, event.x+50, event.y+50, fill="red")
        cercles.append(identifiant)
    elif nb_clic == 9:
        for identifiant in cercles:
            mon_canvas.itemconfigure(identifiant, fill="yellow")
    else:
        for identifiant in cercles:
            mon_canvas.delete(identifiant)
        cercles = []
        nb_clic = 0



racine = tk.Tk()
W = 500
H = 500
mon_canvas = tk.Canvas(racine, background="black", width=W, height=H)
mon_canvas.grid()


mon_canvas.create_rectangle(W//2-50, H//2-50, W//2+50, H//2+50, fill="white")


mon_canvas.bind("<Button-1>", gerer_cercle)


racine.mainloop()
