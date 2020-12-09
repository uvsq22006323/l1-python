print("I LOVE ROCK N ROLL")


carré_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

# carré_pas_mag = carré_mag.copy()

carré_pas_mag = []
for element in carré_mag:
    carré_pas_mag.append(element.copy())



carré_pas_mag[3][2] = 7
print(carré_mag)
print(carré_pas_mag)

# 4
# Créer une fonction qui affiche la liste comme un carré.


def afficheCarré(carré):
    for ligne in carré:
        print(ligne)
    print()


afficheCarré(carré_mag)
afficheCarré(carré_pas_mag)


# 5

# Ecrire une fonction qui teste si les lignes du carré ont toutes la même
# somme. Cette fonction renvoie cette somme si c'est le cas, et -1 sinon.

def testLignesEgales(carre):
    """Renvoie la somme des éléments d'une ligne de la liste 2D carre si tt
    lignes ont la mm somme et -1 sinon"""
    for ligne in carre:
        print(sum(ligne))


print(testLignesEgales(carré_mag))
print(testLignesEgales(carré_pas_mag))
