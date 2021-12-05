# Part 1
file = open("day1/input.txt", "r")

notDone = True

isHigher = 0
prevItem = -1

while notDone:
    input = file.readline().rstrip("\n")
    print(input)
    if input == '':
        print("end of file")
        break
    else:
        input = int(input)

    if prevItem == -1:
        print("first")
    elif input > prevItem:
        isHigher += 1

    prevItem = input

print("-------")
print(isHigher, "readings are higher")

file.close()

