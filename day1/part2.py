groups = []

with open("input.txt", "r") as f:
    smallGroup = []
    for line in f:
        if len(smallGroup) < 3:
            groups.append(int(line))

print(groups)

higher = 0
prevTotal = 0
for i in range(len(groups)):
    if i + 2 > len(groups) - 1:
        break
    total = groups[i] + groups[i+1] + groups[i+2]
    if prevTotal == 0:
        print("first")
    elif total > prevTotal:
        higher += 1
    prevTotal = total

print(higher)
f.close()

