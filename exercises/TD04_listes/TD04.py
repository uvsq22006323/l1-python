# help me # et avec cours n°6
import random

# 1
L1 = [3, 5, 10]
a = L1
# print(a)

# 2
a.extend([12, 17])  # append avec 1 argument, extend avec pls
# print(a)

# 3
L1[2] = -7
# remove pr enlever précis ; del L1[] si un indice
# print(a)

for i in range(len(a)):
    a[i] = a[i] * 2

# print(a)


# A l'aide d'une boucle for, ajouter la valeur i à l'élément d'indice i de la
# liste.

for i in range(len(L1)):
    L1[i] = L1[i] + i

# print([6, 11, -12, 27, 38])
# print(L1)

# 6

nvl_liste = []

# OU nvl_liste = [random.ranint(10,99) for i in range (10)]


for i in range(10):
    nvl_liste.append(random.randint(10, 99))

nvl_liste.sort()
somme = 0

for i in range(len(nvl_liste)):
    somme += nvl_liste[i]
# print("La somme des évènements de la nouvelle liste est", somme)
# print("et le plus grand nombre de cette liste est", nvl_liste[9])

# 7

nvl_pair = []
nvl_impair = []

# nvl_pair, nvl_impair = [], []


# for element in nvl_liste:
#   if element % 2 == 0
#       nvl_pair.append(element)
#   else:
#       nvl_impair.append(element)


for i in range(len(nvl_liste)):
    if nvl_liste[i] % 2 == 0:
        nvl_pair.append(nvl_liste[i])
    else:
        nvl_impair.append(nvl_liste[i])

# print(nvl_pair, nvl_impair)

# 8

nvl_liste.sort()

liste_triée = sorted(nvl_impair)


# 9

del nvl_liste[0]
# nvl_liste.remove(min(nvl_liste))

del nvl_liste[-1]
# nvl_liste.remove(max(nvl_liste))


# 10
carte = [i for i in range(1, 53)]
print(carte)

# 11
ran = random.randint(0, 51)
print(ran)
cartes = (i for i in range(1, ran + 1))
del carte[0: ran]
carte.extend(cartes)
print(carte)

# run and debug
