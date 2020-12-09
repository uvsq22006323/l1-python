import tkinter as tk

racine = tk.Tk()
racine.title("Titre de fenêtre")  # (titre de la fenêtre)
mon_bouton = tk.Button(racine, text="Mon bouton")  # titre fenêtre, texte
mon_bouton.grid(row=0, column=0)

mon_canvas = tk.Canvas(racine, width=500, height=500, background="black")
mon_canvas.grid(row=0, column=1)


mon_canvas.create_line((0, 0), (500, 500), fill="lime")


racine.mainloop()
