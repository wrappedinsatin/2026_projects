
def ranks(num):
    
    if len(rank) == num and rank[0] == "1":
        rank = ""
        square = 0
    else:
        rank = ""
        square = 1

    while not len(rank) > num:
        rank += str(square)
        square -= 1

        if square < 0:
            square = 1

        if len(rank) == num:
            print(rank)
            break

def chessboard(num):
    rep = 0
    while rep < num:
        ranks(num)
        rep += 1

if __name__ == "__main__":
    chessboard(num)