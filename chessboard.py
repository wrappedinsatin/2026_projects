
def chessboard(num):
    
    rank1 = ""
    rank2 = ""

    for i in range(num):
        if i % 2 == 0: # even or odd
            rank1 += "1"
            rank2 += "0"
        else:
            rank1 += "0"
            rank2 += "1"

    for i in range(num):
        if i % 2 == 0:
            print(rank1)
        else:
            print(rank2)

if __name__ == "__main__":
    chessboard(3)