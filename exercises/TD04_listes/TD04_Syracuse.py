# let it begin

# En partant d'un entier n de départ, on définit une suite d'entiers en
# obtenant chaque nouveau terme à partir du précédent soit en le divisant par 2
# s'il est pair, soit en le multipliant par 3 et en ajoutant 1 s'il est impair.


# Depuis n, si i pair, i / 2. Si i impair, i * 3 + 1


# 1

# n1 = 3
# liste1 = [10, 5, 16, 8, 4, 2, 1, 4]  # -> boucle


# 2


def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_val = []
    nbtours = 0
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        liste_val.append(n)
        nbtours += 1
    return (n, liste_val)


nb = int(input("n = ? "))
print(syracuse(nb))
print(syracuse(3))


# 3

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    liste_non = []
    n = 1
    while n != n_max:
        k, v = syracuse(n)
        if int(k) != 1:
            liste_non.append(n)

        n += 1
    if liste_non == []:
        return(True)
    else:
        return(False)


# print(testeConjecture(10000))


# 4

def tempsVol(n):
    tps_vol = 0
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        tps_vol += 1
    return (tps_vol)


print("Le temps de vol de", 3, "est", tempsVol(3))

# 5


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste_vol = []
    for i in range(2, n_max+1):
        k, v = syracuse(i)
        liste_vol.append(len(v))
    return(liste_vol)


print(max(tempsVolListe(5)))
# print(tempsVolListe(100))


# 6

# Déterminer quel entier entre 1 et 10000 a le plus grand temps de vol
# (réponse 6171 qui a le temps de vol 261).

l1 = []

for i in range(1, 10000):
    k, v = syracuse(i)
    l1.append(len(v))

a = l1.index((max(l1))) + 1
print("Temps de vol maximal  = ", max(l1), "; n initial =", a)


# 7

# L’altitude maximale de l'entier `n` est la plus grande valeur par
# laquelle passe `n` au cours de son vol. Déterminer quel entier entre 1
# et 10000 a la plus grande altitude maximale (réponse 27114424, atteint par
# l'entier 9663). Ne pas hésiter à écrire de nouvelles fonctions pour cela.

def VolMax(n):
    pass
