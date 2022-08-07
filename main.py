 # On importe le module random
import random

# On crée un fonction qui intégrera les cas d'erreur
def demander_nombre(nb_min, nb_max):
    # On déclare le nombre de base à 0 afin de pouvoir entrer dans la condition
    nombre_int = 0

    # Tant que le nombre est égale à 0, on permet au joueur d'enter à nouveau un nombre
    while nombre_int == 0:
        # On pose la question initiale au joueur
        nombre_str = input(f"Quel est le nombre mystère entre {nb_min} et {nb_max} ? ")

        # On impose au joueur entrer un nombre, ce qui permettra d'afficher
        # un message d'erreur si le joueur entre une chaine de caractères
        try:
            nombre_int = int(nombre_str)

        # On capture l'exception afin d'afficher un message d'erreur
        except:
            print("ERREUR : veuillez entrer un nombre.")
            print()
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR : Le nombre doit se trouver entre {nb_min} et {nb_max}.")
                print()
                # On réinitialise ce que le joueur a entré en déclarant
                # que le nombre est égale à 0
                nombre_int = 0
    # On ne souhaite pas sortir de la boucle en cas d'erreur
    # donc on repose immédiatement la question au joueur
    return nombre_int


nombre_min = 1
nombre_max = 20
nombre_mystere = random.randint(nombre_min, nombre_max)
nombre_vies = 4

# BOUCLE WHILE

nombre = 0
vies = nombre_vies

while not nombre == nombre_mystere and vies > 0:
    print(f"Il reste {vies} vie" + "(s)")
    print()
    nombre = demander_nombre(nombre_min, nombre_max)
    if nombre == nombre_mystere:
        print("Bravo, vous avez gagné !")
        print()

    elif nombre < nombre_mystere:
        print("Le nombre mystère est plus grand.")
        print()
        vies -= 1

    else:
        print("Le nombre mystère est plus petit.")
        print()
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu ! Le nombre mystère était {nombre_mystere}.")


# ALTERNATIVE BOUCLE FOR

gagner = False

# On calcule le nombre de vie en définissant que i est égale à 0
# à chaque tour de boucle, i va prendre +1
# on va donc soustraire 1 vie à chaque tour de boucle
for i in range(0, nombre_vies):
    vies = nombre_vies-i
    print(f"Il reste {vies} vie" + "(s)")
    print()
    nombre = demander_nombre(nombre_min, nombre_max)
    if nombre == nombre_mystere:
        print("Bravo, vous avez gagné !")
        print()
        gagner = True
        break

    elif nombre < nombre_mystere:
        print("Le nombre mystère est plus grand.")
        print()

    else:
        print("Le nombre mystère est plus petit.")
        print()

if not gagner:
    print(f"Vous avez perdu ! Le nombre mystère était {nombre_mystere}.")