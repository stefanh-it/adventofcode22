def eval_game(games):
    score: int = 0
    for game in games:
        # A == ROCK == 1
        # B == PAPER == 2
        # C == SCISSOR == 3

        # X == LOST 0
        # Y == DRAW 3
        # Z == WIN 6
        if game[2] == "X":  # LOST
            if game[0] == "A":
                score += 3
            elif game[0] == "B":
                score += 1
            else:
                score += 2
        elif game[2] == "Y":  # DRAW
            if game[0] == "A":
                score += 4
            elif game[0] == "B":
                score += 5
            else:
                score += 6
        elif game[2] == "Z":
            if game[0] == "A":
                score += 6 + 2
            elif game[0] == "B":
                score += 6 + 3
            else:
                score += 6 + 1
    return score


def main(data):
    games = data.splitlines()
    print(eval_game(games))


if __name__ == "__main__":
    main('**kwargs')
