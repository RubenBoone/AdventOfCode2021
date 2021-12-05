with open("input.txt", "r") as f:

    gamma = ""
    epsilon = ""

    zero = 0
    one = 0

    for i in range(len(f.readline().rstrip("\n"))):
        for line in f:
            line = line.rstrip("\n")
            if line[i] == "1":
                one += 1
            else:
                zero += 1
        if one > zero:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        zero = 0
        one = 0
        f.seek(0)

print(gamma)
print(epsilon)

print(int(gamma, 2) * int(epsilon, 2))

f.close()