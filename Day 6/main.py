# Part one of the problem
def partOne():
    f = open("input.txt", "r")
    line = f.readline()

    # magic
    for index, discard in enumerate(line):
        if len(set(line[index:index+4])) == 4: # dear god.
            print(index+4) # 1109, correct
            break
        

# Part two of the problem
def partTwo():
    f = open("input.txt", "r")
    line = f.readline()

    # wait... we just change a number?
    for index, discard in enumerate(line):
        if len(set(line[index:index+14])) == 14:
            print(index+14) # 3965, correct
            break

# Main Program
if __name__ == "__main__":
    partOne()
    print("-----")
    partTwo()
