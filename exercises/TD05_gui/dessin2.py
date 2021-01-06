import tkinter as tk

racine = tk.Tk()
racine.title("Essai dessin")

# choix = tk.Button(racine, text="Choisir une couleur", bg="red")
# choix.grid(row=0, column=1)

b1 = tk.Button(racine, text="red", activeforeground="red", pady=10)
# tk.Button(racine, text="red", activeforeground="red", activebackground="pink"
# pady=10)
b1.grid(row=0, column=1)


canvas = tk.Canvas(racine, width=500, height=500, background="black")
canvas.grid(column=1)

racine.mainloop()
