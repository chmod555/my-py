"""
This simple script returns one out of three results for Tic-Tac-Toe 
(or Xs and Os) game: X for X player, O for O player or D for draw
"""

possible_moves = ("X", "O")
empty = "D"

def check_result(game_result):

    if check_rows(game_result) in possible_moves:
        result = check_rows(game_result)
    elif check_rows(transpond_table(game_result)) in possible_moves:
        result = check_rows(transpond_table(game_result))
    elif check_diagonals(game_result) in possible_moves:
        result = check_diagonals(game_result)
    else:
        result = empty

    return str(result)

def check_rows(game):

    for move in possible_moves:
        for row in game:
            if move*3 == row:
                return move
    return empty

def transpond_table(game):

    new_list = []
    for row in list(map(list, zip(*game))):
        new_list.append("".join(row))
    return new_list

def check_diagonals(game):

    for move in possible_moves:
        if game[0][0] == game[1][1] == game[2][2] == move or game[0][2] == game[1][1] == game[2][0] == move:
            return move
    return empty

if __name__ == '__main__':

    assert check_result([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"

    assert check_result([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"

    assert check_result([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"

    assert check_result([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins"
		
    assert check_result([
        "O.X",
        "XO.",
        "XXO"]) == "O", "Os wins"	
