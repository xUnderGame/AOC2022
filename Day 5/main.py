# Part one of the problem
def partOne():
    f = open("input.txt", "r")
    lines = f.readlines()
    boxes = {
        "1": ["W", "L", "S"],
        "2": ["Q", "N", "T", "J"],
        "3": ["J", "F", "H", "C", "S"],
        "4": ["B", "G", "N", "W", "M", "R", "T"],
        "5": ["B", "Q", "H", "D", "S", "L", "R", "T"],
        "6": ["L", "R", "H", "F", "V", "B", "J", "M"],
        "7": ["M", "J", "N", "R", "W", "D"],
        "8": ["J", "D", "N", "H", "F", "T", "Z", "B"],
        "9": ["T", "F", "B", "N", "Q", "L", "H"],
    }

    for x in range(int(9)):
        boxes[str(x+1)] = list(reversed(boxes[str(x+1)]))

    for line in lines:
        line = line.split()
        for x in range(int(line[1])):
            try:
                toAdd = boxes[str(line[3])][len(boxes[str(line[3])])-1]
                boxes[str(line[5])].append(toAdd)
                del boxes[str(line[3])][len(boxes[str(line[3])])-1]
            except: pass

    for entry in boxes:
        print(boxes[entry]) # LMHTFHQ, wrong. NWDBRSN, wrong. RJVFJHD, wrong. FDHNLBB, wrong. RLFNRTNFB, correct.


# Part two of the problem
def partTwo():
    f = open("input.txt", "r")
    lines = f.readlines()
    boxes = {
        "1": ["W", "L", "S"],
        "2": ["Q", "N", "T", "J"],
        "3": ["J", "F", "H", "C", "S"],
        "4": ["B", "G", "N", "W", "M", "R", "T"],
        "5": ["B", "Q", "H", "D", "S", "L", "R", "T"],
        "6": ["L", "R", "H", "F", "V", "B", "J", "M"],
        "7": ["M", "J", "N", "R", "W", "D"],
        "8": ["J", "D", "N", "H", "F", "T", "Z", "B"],
        "9": ["T", "F", "B", "N", "Q", "L", "H"],
    }

    for x in range(int(9)):
        boxes[str(x+1)] = list(reversed(boxes[str(x+1)]))

    for line in lines:
        line = line.split()
        toAdd = []
        for x in range(int(line[1])):
            try:
                toAdd.append(boxes[str(line[3])][len(boxes[str(line[3])])-1]) 
                del boxes[str(line[3])][len(boxes[str(line[3])])-1]
            except: pass
        boxes[str(line[5])] += list(reversed(toAdd))

    for entry in boxes:
        print(boxes[entry]) #RLFNRTNFB, wrong. MHQTLJRLB, correct.


# Main Program
if __name__ == "__main__":
    partOne()
    print("-----")
    partTwo()
