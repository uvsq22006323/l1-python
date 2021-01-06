import tkinter as tk


nb_clic = 0


def remplir_vider(event):
    global nb_clic
    nb_clic += 1

    if nb_clic % 2 == 1:
        color = "black"
    else:
        color = "white"

    mon_canvas.itemconfigure(carre, fill=color)

    if nb_clic == 10:
        racine.destroy()


racine = tk.Tk()
W = 500
H = 500
mon_canvas = tk.Canvas(racine, background="black", width=W, height=H)
mon_canvas.grid()


mon_canvas.create_rectangle(W//2-50, H//2-50, W//2+50, H//2+50, fill="white")


mon_canvas.bind("<Button-1>", remplir_vider)


racine.mainloop()
