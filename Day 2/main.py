# Part one of the problem
def partOne():
    f = open("input.txt", "r")
    lines = f.readlines()
    
    count = 0
    for line in lines:
        if line[-2] == "X":
            count = count + 1
        elif line[-2] == "Y":
            count = count + 2
        elif line[-2] == "Z":
            count = count + 3

        if (line[0] == "A" and line[-2] == "X") or (line[0] == "B" and line[-2] == "Y") or (line[0] == "C" and line[-2] == "Z"): 
            count = count + 3
        elif (line[0] == "A" and line[-2] == "Y") or (line[0] == "B" and line[-2] == "Z") or (line[0] == "C" and line[-2] == "X"): 
            count = count + 6
        elif (line[0] == "A" and line[-2] == "Z") or (line[0] == "B" and line[-2] == "X") or (line[0] == "C" and line[-2] == "Y"): 
            count = count + 0
        print(count) # 10404


# Part two of the problem
def partTwo():
    f = open("input.txt", "r")
    lines = f.readlines()

    count = 0
    # Screw you, no I'm not doing a switch
    for line in lines:
        # Lose
        if line[-2] == "X":
            if line[0] == "A":
                count+=3
            elif line[0] == "B":
                count+=1
            elif line[0] == "C":
                count+=2
        # Tie
        elif line[-2] == "Y":
            if line[0] == "A":
                count+=4
            elif line[0] == "B":
                count+=5
            elif line[0] == "C":
                count+=6
        # Win
        elif line[-2] == "Z":
            if line[0] == "A":
                count+=8
            elif line[0] == "B":
                count+=9
            elif line[0] == "C":
                count+=7
        print(count) # 10334

# Main Program
if __name__ == "__main__":
    partOne()
    partTwo()
