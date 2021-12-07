from types import resolve_bases


with open("day4/input.txt", "r") as f:

    rolledNrs = f.readline().rstrip("\n").split(",")
    boards = []

    f.readline()
    boardPieces = []
    for line in f:
        if line != "\n":
            numbers = []
            for number in line.rstrip("\n").split(" "):
                if number != '':
                    numbers.append(number)
            boardPieces.append(numbers)
        else:
            boards.append(boardPieces)
            boardPieces = []

    winningBoard = -1
    rolled = -1

    for rollednumber in rolledNrs:
        for i in range(len(boards)):
            if winningBoard != -1:
                break
            for j in range(len(boards[0])):
                if winningBoard != -1:
                    break
                marked = 0
                for x in range(len(boards[0][0])):

                    if boards[i][j][x] == rollednumber:
                        boards[i][j][x] = "-1"

                    if boards[i][j][x] == "-1":
                        marked += 1
                        if marked == 5:
                            winningBoard = i
                            rolled = rollednumber
                            break

                    colum = 0
                    for y in range(5):
                        if boards[i][y][x] == "-1":
                            colum += 1
                            if colum == 5:
                                winningBoard = i
                                rolled = rollednumber
                                break

    sum = 0
    for line in boards[winningBoard]:
        for number in line:
            if number != "-1":
                sum += int(number)

    print(sum, "*", rolled, "=", sum*int(rolled))

f.close()
