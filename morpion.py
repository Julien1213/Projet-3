from helpers import check_turn, check_for_win, draw_board

spots = {7:'7',8:'8',9:'9',10:'',4:'4',5:'5',6:'6',1:'1',2:'2',3:'3'}
continuer, complete = True, False
turn = 0
prev_turn = -1

while continuer:
    draw_board(spots)
    if prev_turn == turn:
        print("Emplacement invalide, veuillez en choisir un autre !")
    prev_turn = turn
    print("Au tour du joueur " + str((turn % 2) +1 ) + ": Choisissez votre emplacement ou tapez Stop pour arrêter le jeu !")

    choix = input()
    if choix == 'Stop':
        continuer = False
    elif str.isdigit(choix) and int(choix) in spots:
        if not spots[int(choix)] in {"X", "O"}:
            turn +=1
            spots[int(choix)] = check_turn(turn)

    if check_for_win(spots):
        continuer, complete = False, True
    if turn > 8:
        continuer = False

draw_board(spots)
if complete:
    if check_turn(turn) == 'X': print("Victoire joueur 1 !")
    else: print("Victoire joueur 2 !")

else:
    print("Egalité !")

print("Merci d'avoir joué au jeu !")

