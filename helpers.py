def draw_board(spots):

    tableau = (f"|{spots[7]}|{spots[8]}|{spots[9]}|{spots[10]}\n"
            f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
            f"|{spots[1]}|{spots[2]}|{spots[3]}|")
    print(tableau)

def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    
    else:
        return 'X'

def check_for_win(spots):
    if   (spots[7] == spots[8] == spots[9]) \
      or (spots[4] == spots[5] == spots[6]) \
      or (spots[1] == spots[2] == spots[3]) \
      or (spots[8] == spots[9] == spots[10]):
      return True
    elif (spots[7] == spots[4] == spots[1]) \
      or (spots[8] == spots[5] == spots[2]) \
      or (spots[9] == spots[6] == spots[3]):
      return True
    elif (spots[7] == spots[5] == spots[3]) \
      or (spots[9] == spots[5] == spots[1]) \
      or (spots[2] == spots[6] == spots[10]):
      return True

    else:
        return False

