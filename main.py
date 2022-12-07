import os, sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    data = [l.strip() for l in f.readlines()]
    # Part 1
    fs = {}
    fs["/"] = []
    current = ""
    for i in data:
        if i[0] == "$":
            cmd = i[2:4]
            if cmd == "cd":
                dirChange = i[5:]
                if dirChange == "/" or (dirChange == ".." and current == ""):
                    current = ""
                elif dirChange == "..":
                    currentSplit = current.split("/")
                    currentSplit.pop()
                    current = "/".join(currentSplit)
                else:
                    current = f"{current}/{dirChange}"
        elif i[0:3] == "dir":
            dirGiven = i[4:]
            if f"{current}/{dirGiven}" not in fs:
                fs[f"{current}/{dirGiven}"] = []
        else:
            if current == "":
                fs["/"].append(i)
            else:
                fs[current].append(i)
    sums = {}
    for k,v in fs.items():
        for i in v:
            size = int(i.split(" ")[0])
            dirSplit = k.split("/")
            if k != "/":
                dirSplit.pop(0)
                for j in range(len(dirSplit)):
                    toAdd = "/".join(dirSplit[0:j+1]) if j > 0 else dirSplit[0]
                    if toAdd not in sums:
                        sums[toAdd] = 0
                    sums[toAdd] += size
            if "/" not in sums:
                sums["/"] = 0
            sums["/"] += size
    print(sum([i for i in sums.values() if i < 100000]))
    # Part 2
    total = sums["/"]
    unused = 70000000-total
    needed = 30000000-unused
    print(min([i for i in sums.values() if i >= needed]))