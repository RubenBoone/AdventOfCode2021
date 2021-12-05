horizontal = 0
depth = 0

with open("input.txt", "r") as f:
    for line in f:
        instruction = line.rstrip("\n").split(" ")
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
        if instruction[0] == "down":
            depth += int(instruction[1])
        if instruction[0] == "up":
            depth -= int(instruction[1])

print(depth * horizontal)

f.close()