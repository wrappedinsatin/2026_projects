
def ranks(num):

    while not len(rank) > num:
        rank += str(square)
        square -= 1

        if square < 0:
            square = 1

        if len(rank) == num:
            print(rank)
            break

    return rank

def repeat(rank):

    if rank[0] == "0":
        rank = ""
        square = 0
        ranks(num)

    else:
        rank = ""
        square = 1
        ranks(num)

def chessboard(num):
    rep = 0
    while rep < num:
        repeat(rank)
        rep += 1

if __name__ == "__main__":
    chessboard(num)