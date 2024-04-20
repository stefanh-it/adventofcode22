def eval_game(games):
    score: int = 0
    for game in games:
        # A == ROCK
        # B == PAPER
        # C == SCISSOR

        # X == ROCK 1
        # Y == PAPER 2
        # Z == SCISSOR 3

        if game[0] == 'A' and game[2] == 'X':  # DRAW
            score += 1 + 3
        elif game[0] == 'B' and game[2] == 'Y':  # DRAW
            score += 2 + 3
        elif game[0] == 'C' and game[2] == 'Z':  # DRAW
            score += 3 + 3
        elif game[0] == 'A' and game[2] == 'Y':  # WIN
            score += 2 + 6
        elif game[0] == 'B' and game[2] == 'Z':  # WIN
            score += 3 + 6
        elif game[0] == 'C' and game[2] == 'X':  # WIN
            score += 1 + 6
        elif game[2] == 'X':
            score += 1
        elif game[2] == 'Y':
            score += 2
        elif game[2] == 'Z':
            score += 3
    return score


def main(data):
    games = data.splitlines()
    print(eval_game(games))


if __name__ == "__main__":
    main('**kwargs')
