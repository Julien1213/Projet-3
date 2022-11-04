from random import randint

jeu = ["pierre", "papier", "ciseaux"]

IA = jeu[randint(0,2)]

PointsJ1 = 0
PointsIA = 0

continuer = True

while(continuer):
    J1 = input("Bienvenue dans le jeu pierre papier ciseaux !\nChoississez entre pierre, papier et ciseaux ? ou tapez Stop pour arrêter le jeu !\n")

    if(J1 == 'Stop'):
        continuer = False
    elif(J1 == IA):
        print("Egalité !")
    elif(J1 == "pierre"):
        if(IA == "papier"):
            print("Dommage vous avez perdu !", "Le papier recouvre la pierre !")
            PointsIA = PointsIA + 1
        else:
            print("Bravo vous avez gagné !", "La pierre casse les ciseaux !")
            PointsJ1 = PointsJ1 + 1
    elif(J1 == "papier"):
        if(IA == "ciseaux"):
            print("Dommage vous avez perdu !", "Les ciseaux coupent le papier !")
            PointsIA = PointsIA + 1
        else:
            print("Bravo vous avez gagné !", "Le papier recouvre la pierre !")
            PointsJ1 = PointsJ1 + 1
    elif(J1 == "ciseaux"):
        if(IA == "pierre"):
            print("Dommage vous avez perdu !", "La pierre casse les ciseaux !")
            PointsIA = PointsIA + 1
        else:
            print("Bravo vous avez gagné !", "Les ciseaux coupent le papier !")
            PointsJ1 = PointsJ1 + 1
    else:
        print("Incorrecte")
    IA = jeu[randint(0,2)]
    print('--------PROCHAINE MANCHE--------')

print("--------RESULTATS--------")
print("J1: ", PointsJ1)
print("IA: ", PointsIA)

