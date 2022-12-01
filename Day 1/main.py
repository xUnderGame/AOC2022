
def partOne():
    f = open("input.txt", "r")
    max = 0
    calCount = 0

    lines = f.readlines()
    for calories in lines:
        if calories == "\n" or calories == "":
            if calCount > max:
                max=calCount
            calCount = 0
        else:
            calCount = calCount + int(calories)
    print(max) # 69177

def partTwo():
    f = open("input.txt", "r")
    max = [0]
    calCount = 0

    lines = f.readlines()
    for calories in lines:
        if calories == "" or calories == "\n":
            max.append(calCount)
            calCount = 0
        else:
            calCount += int(calories)
    max.sort(reverse=True)
    print(max[0]+max[1]+max[2]) # 207456

partOne()
partTwo()