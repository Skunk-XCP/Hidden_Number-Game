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

        # Si le joueur entre un nombre qui est inférieur ou supérieur à la fourchette établie
        # on lui indiquera alors son erreur
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

# On établie la fourchette dans laquelle le joueur devra trouver le nombre mystère
nombre_min = 1
nombre_max = 20

# On crée le nombre mystère avec le module random en précisant dans les paramètres
# la fourchette établie
nombre_mystere = random.randint(nombre_min, nombre_max)

# On établie un système de vie qui sera le nombre de chance
# que le joueur aura pour trouver le nombre mystère
nombre_vies = 4

# BOUCLE WHILE

# On déclare le nombre à 0 afin de pouvoir l'utiliser dans la condition
nombre = 0
vies = nombre_vies

# Tant que le nombre n'est pas égale au chiffre mystère
# et que le nombre de vies est supérieur à 0
# alors on demande au joueur le nombre mystère
# et on lui indique son nombre de vie
while not nombre == nombre_mystere and vies > 0:
    print(f"Il reste {vies} vie" + "(s)")
    print()
    nombre = demander_nombre(nombre_min, nombre_max)

    # On compare le nombre entré par le joueur avec le nombre mystère
    # Si celui-ci correspond, alors on affiche un message de réussite
    # Et on sort de la boucle
    if nombre == nombre_mystere:
        print("Bravo, vous avez gagné !")
        print()

    # Si le nombre entré est plus petit que le nombre mystère
    # Alors on indique au joueur que le nombre qu'il cherche est plus grand
    elif nombre < nombre_mystere:
        print("Le nombre mystère est plus grand.")
        print()
        # On retire une vie au joueur
        vies -= 1

    # Si le nombre entré est plus grand que le nombre mystère
    # Alors on indique au joueur que le nombre qu'il cherche est plus petit
    else:
        print("Le nombre mystère est plus petit.")
        print()
        # On retire une vie au joueur
        vies -= 1

# Si le nombre de vie atteind 0, on dignale au joueur qu'il a perdu, et on lui révèle le nombre mystère
if vies == 0:
    print(f"Vous avez perdu ! Le nombre mystère était {nombre_mystere}.")


# ALTERNATIVE BOUCLE FOR

# On crée une variable booléenne qui nous permettra, en cas de défaite,
# d'afficher le message correspondant
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

          # La variable booléenne nous permettra de ne pas afficher le message
          # de défaite en cas de victoire
        gagner = True

          # Le break nous permet de sortir de la boucle
        break
    elif nombre < nombre_mystere:
        print("Le nombre mystère est plus grand.")
        print()
    else:
        print("Le nombre mystère est plus petit.")
        print()

if not gagner:
    print(f"Vous avez perdu ! Le nombre mystère était {nombre_mystere}.")