# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes
# liens utiles : https://www.epochconverter.com/ ;
# https://www.calendar-365.com/

import time


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné
    comme jour, heure, minute, seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]


# temps = [3, 23, 1, 34]
# print(type(temps))
# print(tempsEnSeconde(temps))

# raccourci linter Python : Ctrl + shift + P -> flake8  ou  mypy


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui
    correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    reste = seconde % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    return (jours, heures, minutes, reste)


seconde = secondeEnTemps(100000)
# print(temps[0], "jours", temps[1], "heures", temps[2], "minutes",
#                 temps[3], "secondes")


# afficheTemps()

def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    print()


def affichePluriel(mot, nombre):
    if nombre > 0:
        print(" ", nombre, mot, end="")
    if nombre > 1:
        print("s", end="")


# afficheTemps((1, 0, 14, 23))  # 1j 0h 14m 23s

# demandeTemps()


def demandeTemps(tmps):
    J = -1
    H = -1
    M = -1
    S = -1

    while J < 0:
        J = int(input("Veuillez entrer votre nombre de jour svp."))
    while (H < 0) or (H >= 24):
        H = int(input("Veuillez entrer votre nombre d'heures svp."))
    while (M > 0) or (M >= 60):
        M = int(input("Veuillez entrer votre nombre de minutes svp."))
    while (S < 0) or (S >= 60):
        S = int(input("Veuillez entrer votre nombre de secondes svp."))

    print(J, "jours", H, "heures", M, "minutes", S, "secondes")


# afficheTemps(demandeTemps())
# print(tmps)


# sommeTemps()

def sommeTemps(temps1, temps2):
    a = temps1[0] + temps2[0]
    b = temps1[1] + temps2[1]
    c = temps1[2] + temps2[2]
    d = temps1[3] + temps2[3]
    sommeTemps = (a, b, c, d)
    return(secondeEnTemps(sommeTemps))


# afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


# proportionTemps()

# IL FAUT SE SERVIR DES PRÉCÉDENTES FONCTIONS

def proportionTemps(temps: tuple, proportion: float) -> tuple:
    """ Retourne un temps égal au temps passé en paramètres
    après application de la proportion"""

    return secondeEnTemps(int(tempsEnSeconde(temps) * proportion))


# afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))
# appeler la fonction en échangeant l'ordre des arguments


# tempsEnDate()


def tempsEnDate(temps):
    année = temps[0] // 365
    jours = temps[0] % 365
    return (1970 + année, 1 + jours, temps[1], temps[2], temps[3])

# afficheDate(date: tuple = ()) -> fonction prend un paramètre de type
# tuple ; peut être omis -> prendra pour valeur(), un tuple vide


def afficheDate(date: tuple = ()):
    if len(date) == 0:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("Année", date[0], "Jour", date[1], str(date[2]), ":" + str(date[3])
                            + ":" + str(date[4]))


# temps = secondeEnTemps(86401)
# afficheTemps(temps)
# afficheDate(tempsEnDate(temps))
# afficheDate()

# print(time.time())
# afficheDate()


def bissextile(jour):
    année = 1970
    compteur_bissextile = 0
    while (jour >= 365):
        if année % 4 == 0 and (année % 100 != 0 or année % 400 == 0):
            compteur_bissextile += 1
            jour -= 366
        else:
            jour -= 365
        année += 1
    return(compteur_bissextile)


def tempsEnDateBissextile(temps):
    jour, heure, minute, seconde = temps
    jour = jour - bissextile(jour)
    temps_ajusté = (jour, heure, minute, seconde)
    return tempsEnDate(temps_ajusté)


# afficheDate(tempsEnDateBissextile(secondeEnTemps(int(time.time()))))


# verifie(liste_temps)

# (Optionnel) S'adapter à une liste qui peut contenir plusieurs mois.

def verifie(liste_temps):
    employéS = []
    employéM = []
    compteur_mois = 0
    for i in range(len(liste_temps)):
        for j in liste_temps[i]:
            if j > 48:
                employéS.append(i)
        compteur_mois += j
    if compteur_mois > 140:
        employéM.append[i]
    return(employéS, employéM)


liste_temps = [[1, 2, 39, 34], [0, 1, 9, 4], [0, 29, 39, 51], [0, 31, 13, 46]]
verifie(liste_temps)
# print("L'(es) employé(s)", employéS, "ont dépassé 48h par semaine,")
# print("Les employés", employéM, "ont dépassé 140h par semaine.")
