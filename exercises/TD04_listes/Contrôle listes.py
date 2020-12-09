# Ecrire la fonction carre_decroissant( n ) qui prend en argument un
# entier positif n et retourne la liste constituée des n listes
# imbriquées suivante:

# [[n, n+1, ..., 2*n-1], [n-1, n, ..., 2*n-2], [n-2, n-1, ..., 2*n-3], ...,
# [2, 3, ..., n+1], [1, 2, ..., n]]

# où les points de suspension "..." désignent la suite des entiers consécutifs.
# Par exemple, [1,2, ..., 5] désigne la suite [1, 2, 3, 4, 5].


# Ecrire le code qui construit la liste qui contient tous les entiers
# pairs de 0 à 100 (bornes incluses) suivis de tous les entiers de 99
# jusqu'à 1 (bornes incluses).


def plus_3(liste):
    for i in liste:
        i = i + 3
    print(liste)


liste1 = [10, 6, 7]
plus_3(liste1)
