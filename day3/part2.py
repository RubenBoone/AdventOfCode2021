def makeArraySmallerPriorityOne(i, newArray):
    ones = []
    zeros = []
    one = 0
    zero = 0

    for item in newArray:
        if item[i] == "1":
            one += 1
            ones.append(item)
        else:
            zero += 1
            zeros.append(item)

    if one < zero:
        return ones
    else:
        return zeros


def makeArraySmallerPriorityZero(i, newArray):
    ones = []
    zeros = []
    one = 0
    zero = 0

    for item in newArray:
        if item[i] == "1":
            one += 1
            ones.append(item)
        else:
            zero += 1
            zeros.append(item)

    if one > zero:
        return ones
    else:
        return zeros


def whichHigher(i, list):
    one = 0
    zero = 0

    ones = []
    zeros = []

    for item in list:
        if item[i] == '1':
            one += 1
            ones.append(item)
        else:
            zero += 1
            zeros.append(item)

    if zero > one:
        return zeros
    else:
        return ones


def whichLower(i, list):
    one = 0
    zero = 0

    ones = []
    zeros = []

    for item in list:
        if item[i] == '1':
            one += 1
            ones.append(item)
        else:
            zero += 1
            zeros.append(item)

    if one < zero:
        return ones
    else:
        return zeros


with open("day3/input.txt", "r") as f:

    one = 0
    zero = 0

    fullList = []
    list = []

    for line in f:
        fullList.append(line.rstrip("\n"))

    list = fullList

    for i in range(0, len(list[0])):
        list = whichHigher(i, list)
        if len(list) == 1:
            break

    o2 = int(list[0], 2)

    list = fullList

    for i in range(0, len(list[0])):
        list = whichLower(i, list)
        if len(list) == 1:
            break

    co2 = int(list[0], 2)

    print(o2 * co2)

f.close()
